from django.urls import path
from . import views

urlpatterns = [

    path(
        '',
        views.tourism_home,
        name='tourism_home'
    ),

    path(
        '<slug:slug>/',
        views.attraction_detail,
        name='attraction_detail'
    ),

    path(
        'category/<str:category>/',
        views.attraction_category,
        name='attraction_category'
    ),

]