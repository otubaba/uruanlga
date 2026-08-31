from django.shortcuts import render, get_object_or_404
from .models import Gallery


def gallery_list(request):

    galleries = Gallery.objects.all()

    return render(
        request,
        'gallery/gallery_list.html',
        {
            'galleries': galleries
        }
    )


def gallery_detail(request, slug):

    gallery = get_object_or_404(
        Gallery,
        slug=slug
    )

    return render(
        request,
        'gallery/gallery_detail.html',
        {
            'gallery': gallery
        }
    )