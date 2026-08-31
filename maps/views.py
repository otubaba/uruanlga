from django.shortcuts import render
from .models import Location


def uruan_map(request):

    locations = Location.objects.all()

    return render(
        request,
        'maps/uruan_map.html',
        {
            'locations': locations
        }
    )