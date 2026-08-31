from django.shortcuts import render, get_object_or_404
from .models import News, Category
from django.core.paginator import Paginator
from django.db.models import Q
from about.models import ProminentIndigene


def home(request):

    # ---------------------------------------------------------
    # FEATURED NEWS
    # ---------------------------------------------------------
    featured_news = (
        News.objects
        .filter(
            featured=True,
            status="Published"
        )
        .order_by("-published_at")[:3]
    )

    # ---------------------------------------------------------
    # LATEST NEWS
    # ---------------------------------------------------------
    latest_news = (
        News.objects
        .filter(status="Published")
        .order_by("-published_at")[:9]
    )

    # ---------------------------------------------------------
    # NEWS CATEGORIES
    # ---------------------------------------------------------
    categories = Category.objects.all()

    # ---------------------------------------------------------
    # PROMINENT INDIGENES
    # ---------------------------------------------------------
    prominent_indigenes = (
        ProminentIndigene.objects
        .filter(is_active=True)
        .order_by("display_order", "name")[:8]
    )

    # ---------------------------------------------------------
    # CONTEXT
    # ---------------------------------------------------------
    context = {
        
        "featured_news": featured_news,
        "latest_news": latest_news,
        "categories": categories,
        "prominent_indigenes": prominent_indigenes,
    }

    return render(
        request,
        "news/home.html",
        context
    )

def news_list(request):

    news = News.objects.filter(
        status='Published'
    )

    return render(
        request,
        'news/news_list.html',
        {'news': news}
    )


def news_detail(request, slug):

    post = get_object_or_404(
        News,
        slug=slug,
        status="Published"
    )

    # Increment views
    post.views += 1
    post.save(update_fields=["views"])

    related_posts = News.objects.filter(
        status="Published",
        category=post.category
    ).exclude(
        pk=post.pk
    )[:4]

    context = {
        "post": post,
        "related_posts": related_posts,
    }

    return render(
        request,
        "news/news_detail.html",
        context
    )

def category_posts(request, slug):

    # Get the category
    category = get_object_or_404(
        Category,
        slug=slug
    )

    # Get published news in this category
    posts = (
        News.objects
        .filter(
            category=category,
            status="Published"
        )
        .select_related(
            "category",
            "author"
        )
        .order_by("-created_at")
    )

    # Pagination
    paginator = Paginator(posts, 9)

    page_number = request.GET.get("page")

    page_obj = paginator.get_page(page_number)

    context = {
        "category": category,
        "posts": page_obj,
        "page_obj": page_obj,
    }

    return render(
        request,
        "news/category_posts.html",
        context
    )


def search(request):

    query = request.GET.get("q", "").strip()

    results = News.objects.none()

    if query:
        results = News.objects.filter(
            status="Published"
        ).filter(
            Q(title__icontains=query) |
            Q(summary__icontains=query) |
            Q(content__icontains=query)
        ).select_related(
            "category",
            "author"
        )

    context = {
        "query": query,
        "results": results,
    }

    return render(
        request,
        "news/search_results.html",
        context
    )
