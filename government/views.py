from django.shortcuts import render, get_object_or_404
from .models import CouncilLeadership, PastChairman, TraditionalLeader



def chairman_message(request):

    chairman = CouncilLeadership.objects.filter(
        council_type="Executive",
        designation__iexact="Executive Chairman",
        current=True,
        show_chairman_message=True,
    ).first()

    return render(
        request,
        "government/chairman_message.html",
        {
            "chairman": chairman,
        }
    )


def past_chairman_list(request):

    chairmen = PastChairman.objects.filter(
        featured=True
    ).order_by(
        '-tenure_end',
        'order',
        'full_name'
    )

    return render(
        request,
        'government/chairman_list.html',
        {
            'chairmen': chairmen
        }
    )


def past_chairman_detail(request, slug):

    chairman = get_object_or_404(
        PastChairman,
        slug=slug,
        featured=True
    )

    # Other former chairmen
    related_chairmen = PastChairman.objects.filter(
        featured=True
    ).exclude(
        pk=chairman.pk
    ).order_by(
        '-tenure_end',
        'order',
        'full_name'
    )[:4]

    context = {
        'chairman': chairman,
        'related_chairmen': related_chairmen,
    }

    return render(
        request,
        'government/chairman_detail.html',
        context
    )


def executive_leadership(request):

    executives = (
        CouncilLeadership.objects
        .filter(council_type="Executive")
        .order_by("-current", "order", "-created_at")
    )

    current_chairman = (
        CouncilLeadership.objects
        .filter(
            council_type="Executive",
            designation__icontains="Chairman",
            current=True,
        )
        .order_by("order", "-created_at")
        .first()
    )

    context = {
        "executives": executives,
        "current_chairman": current_chairman,
    }

    return render(
        request,
        "government/executive_leadership.html",
        context
    )


def executive_leadership_detail(request, slug):

    leader = get_object_or_404(
        CouncilLeadership,
        slug=slug,
        council_type="Executive"
    )

    return render(
        request,
        "government/executive_leadership_detail.html",
        {
            "leader": leader,
        }
    )


def legislative_leadership(request):

    legislators = (
        CouncilLeadership.objects
        .filter(council_type="Legislative")
        .order_by("-current", "order", "-created_at")
    )

    context = {
        "legislators": legislators,
    }

    return render(
        request,
        "government/legislative_leadership.html",
        context
    )

def legislative_leadership_detail(request, slug):
    leader = get_object_or_404(
        CouncilLeadership,
        slug=slug,
        council_type="Legislative"
    )

    return render(
        request,
        "government/legislative_leadership_detail.html",
        {
            "leader": leader,
        }
    )

def traditional_leader_list(request):
    """
    Display all featured traditional leaders.
    """

    leaders = TraditionalLeader.objects.filter(
        featured=True
    ).order_by(
        'order',
        'full_name'
    )

    context = {
        'leaders': leaders,
    }

    return render(
        request,
        'government/traditional_leader_list.html',
        context
    )


def traditional_leader_detail(request, slug):
    """
    Display the profile of a traditional leader.
    """

    leader = get_object_or_404(
        TraditionalLeader,
        slug=slug,
        featured=True
    )

    context = {
        'leader': leader,
    }

    return render(
        request,
        'government/traditional_leader_detail.html',
        context
    )
