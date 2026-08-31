from django.urls import path
from . import views

urlpatterns = [

    path(
        '',
        views.uruan_map,
        name='uruan_map'
    ),

]