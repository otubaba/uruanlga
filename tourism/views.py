from django.shortcuts import render, get_object_or_404
from .models import Attraction

def tourism_home(request):

    attractions = Attraction.objects.all()

    context = {
        'attractions': attractions
    }

    return render(
        request,
        'tourism/tourism_home.html',
        context
    )


def attraction_detail(request, slug):

    attraction = get_object_or_404(
        Attraction,
        slug=slug
    )

    related_places = Attraction.objects.filter(
        category=attraction.category
    ).exclude(
        id=attraction.id
    )[:4]

    context = {
        'attraction': attraction,
        'related_places': related_places
    }

    return render(
        request,
        'tourism/attraction_detail.html',
        context
    )

def attraction_category(request, category):

    attractions = Attraction.objects.filter(
        category=category
    )

    return render(
        request,
        'tourism/category.html',
        {
            'attractions': attractions,
            'category': category
        }
    )

