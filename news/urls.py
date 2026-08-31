from django.urls import path
from . import views


app_name = 'news'

urlpatterns = [

    path(
        '',
        views.news_list,
        name='news_list'
    ),

    path(
        'news/<slug:slug>/',
        views.news_detail,
        name='news_detail'
    ),

    path(
        'category/<slug:slug>/',
        views.category_posts,
        name='category_posts'
    ),

    path(
    'search/',
    views.search,
    name='search'
    ),

]