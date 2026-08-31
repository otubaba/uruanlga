from django.shortcuts import render

from news.models import News, BreakingNews
from projects.models import Project
from tourism.models import Attraction
from government.models import CouncilLeadership
from about.models import ProminentIndigene, HomeHero


def home(request):

    # =========================================================
    # LATEST NEWS
    # =========================================================

    latest_news = (
        News.objects
        .filter(status="Published")
        .order_by("-created_at")[:6]
    )

    latest_posts = latest_news

    # =========================================================
    # FEATURED PROJECTS
    # =========================================================

    projects = (
        Project.objects
        .filter(featured=True)
        .order_by("-created_at")[:4]
    )

    # =========================================================
    # FEATURED TOURIST ATTRACTIONS
    # =========================================================

    attractions = (
        Attraction.objects
        .filter(featured=True)
        .order_by("-created_at")[:4]
    )

    # =========================================================
    # CURRENT EXECUTIVE CHAIRMAN
    # =========================================================

    chairman = (
        CouncilLeadership.objects
        .filter(
            council_type="Executive",
            designation__icontains="Chairman",
            current=True,
            show_chairman_message=True,
        )
        .order_by("order", "-created_at")
        .first()
    )

    # =========================================================
    # PROMINENT INDIGENES
    # =========================================================

    prominent_indigenes = (
        ProminentIndigene.objects
        .all()
        .order_by("order", "name")[:8]
    )

    # =========================================================
    # BREAKING NEWS
    # =========================================================

    breaking_news = BreakingNews.objects.filter(
        active=True
    ).order_by('-id')[:10]

    # =========================================================
    # HOME HERO
    # =========================================================

    hero = (
        HomeHero.objects
        .filter(is_active=True)
        .prefetch_related("stats")
        .first()
    )

    # =========================================================
    # CONTEXT
    # =========================================================

    context = {
        "latest_posts": latest_posts,
        "latest_news": latest_news,
        "projects": projects,
        "attractions": attractions,
        "chairman": chairman,
        "breaking_news": breaking_news,
        "prominent_indigenes": prominent_indigenes,
        "hero": hero,
    }

    return render(request, "index.html", context)

