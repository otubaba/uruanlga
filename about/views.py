from django.shortcuts import render, get_object_or_404
from .models import AboutSection


def about_home(request):

    sections = AboutSection.objects.all()

    return render(
        request,
        'about/about_home.html',
        {
            'sections': sections
        }
    )



def about_detail(request, slug):

    section = get_object_or_404(
        AboutSection,
        slug=slug
    )

    sections = AboutSection.objects.all()

    return render(
        request,
        'about/about_detail.html',
        {
            'section': section,
            'sections': sections,
        }
    )

from django.shortcuts import get_object_or_404, render

from .models import ProminentIndigene


def prominent_indigene_detail(request, slug):

    indigene = get_object_or_404(
        ProminentIndigene,
        slug=slug,
        featured=True
    )

    return render(
        request,
        "about/prominent_indigene_detail.html",
        {
            "indigene": indigene,
        }
    )

