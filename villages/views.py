from django.shortcuts import render, get_object_or_404
from django.db.models import Q, Count

from .models import (
    ClanCategory,
    Clan,
    Ward,
    Village,
)


# ================================================================
# CLAN CATEGORY LIST
# ================================================================

def clan_category_list(request):

    categories = (
        ClanCategory.objects
        .annotate(
            clan_count=Count("clans", distinct=True)
        )
        .order_by("name")
    )

    return render(
        request,
        "villages/clan_category_list.html",
        {
            "categories": categories,
        }
    )


def clan_category_detail(request, slug):

    category = get_object_or_404(
        ClanCategory,
        slug=slug
    )

    clans = (
        category.clans
        .prefetch_related(
            "wards__villages"
        )
        .all()
    )

    # Count wards and villages belonging to this category
    ward_count = sum(
        clan.wards.count()
        for clan in clans
    )

    village_count = sum(
        ward.villages.count()
        for clan in clans
        for ward in clan.wards.all()
    )

    return render(
        request,
        "villages/clan_category_detail.html",
        {
            "category": category,
            "clans": clans,
            "ward_count": ward_count,
            "village_count": village_count,
        }
    )


def clan_detail(request, slug):

    clan = get_object_or_404(
        Clan.objects.select_related("category"),
        slug=slug
    )

    wards = (
        clan.wards
        .prefetch_related("villages")
        .all()
    )

    village_count = sum(
        ward.villages.count()
        for ward in wards
    )

    return render(
        request,
        "villages/clan_detail.html",
        {
            "clan": clan,
            "wards": wards,
            "village_count": village_count,
        }
    )


def ward_detail(request, clan_slug, slug):

    ward = get_object_or_404(
        Ward.objects.select_related("clan", "clan__category"),
        slug=slug,
        clan__slug=clan_slug,
    )

    villages = (
        ward.villages
        .order_by("name")
    )

    # Previous and next villages
    previous_village = (
        villages.filter(name__lt=villages.first().name)
        .order_by("-name")
        .first()
        if villages.exists()
        else None
    )

    next_village = (
        villages.filter(name__gt=villages.last().name)
        .order_by("name")
        .first()
        if villages.exists()
        else None
    )

    context = {
        "ward": ward,
        "villages": villages,
        "village_count": villages.count(),
        "clan": ward.clan,
        "category": ward.clan.category,
        "previous_village": previous_village,
        "next_village": next_village,
    }

    return render(
        request,
        "villages/ward_detail.html",
        context
    )

# ================================================================
# CLAN LIST
# ================================================================

def clan_list(request):

    categories = (
        ClanCategory.objects
        .prefetch_related("clans")
        .order_by("name")
    )

    return render(
        request,
        "villages/clan_list.html",
        {
            "categories": categories,
        }
    )




# ================================================================
# VILLAGE LIST
# ================================================================

def village_list(request):

    search_query = request.GET.get("q", "").strip()
    clan_filter = request.GET.get("clan", "").strip()

    villages = (
        Village.objects
        .select_related("clan", "ward")
        .all()
    )

    # ------------------------------------------------------------
    # SEARCH
    # ------------------------------------------------------------

    if search_query:

        villages = villages.filter(
            Q(name__icontains=search_query)
            |
            Q(description__icontains=search_query)
        )


    # ------------------------------------------------------------
    # CLAN FILTER
    # ------------------------------------------------------------

    if clan_filter:

        if clan_filter.isdigit():

            villages = villages.filter(
                clan_id=clan_filter
            )

        else:

            villages = villages.filter(
                clan__name__icontains=clan_filter
            )


    # ------------------------------------------------------------
    # CLANS FOR FILTER DROPDOWN
    # ------------------------------------------------------------

    clans = Clan.objects.order_by("name")


    villages = villages.order_by("name")


    context = {
        "villages": villages,
        "search_query": search_query,
        "clan_filter": clan_filter,
        "clans": clans,
        "total_count": villages.count(),
    }


    return render(
        request,
        "villages/village_list.html",
        context
    )


# ================================================================
# VILLAGE DETAIL
# ================================================================

def village_detail(request, slug, ward_slug):

    village = get_object_or_404(
        Village.objects.select_related(
            "ward",
            "ward__clan",
            "ward__clan__category",
        ),
        slug=slug,
        ward__slug=ward_slug,
    )

    # Other villages in the same ward
    related_villages = (
        Village.objects
        .filter(ward=village.ward)
        .exclude(pk=village.pk)
        .order_by("name")[:4]
    )

    # Previous village in the same ward
    previous_village = (
        Village.objects
        .filter(
            ward=village.ward,
            name__lt=village.name,
        )
        .order_by("-name")
        .first()
    )

    # Next village in the same ward
    next_village = (
        Village.objects
        .filter(
            ward=village.ward,
            name__gt=village.name,
        )
        .order_by("name")
        .first()
    )

    # Related posts, if Village has a posts related_name
    related_posts = None

    if hasattr(village, "posts"):
        related_posts = (
            village.posts
            .filter(status="published")
            .order_by("-created_at")[:5]
        )

    context = {
        "village": village,
        "related_villages": related_villages,
        "previous_village": previous_village,
        "next_village": next_village,
        "related_posts": related_posts,
    }

    return render(
        request,
        "villages/village_detail.html",
        context,
    )
