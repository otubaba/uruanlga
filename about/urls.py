from django.urls import path
from . import views

urlpatterns = [

    path(
        '',
        views.about_home,
        name='about_uruan'
    ),

    path(
        '<slug:slug>/',
        views.about_detail,
        name='about_detail'
    ),
    path(
        "prominent-indigenes/<slug:slug>/",
        views.prominent_indigene_detail,
        name="prominent_indigene_detail"
    ),

]