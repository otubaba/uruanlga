from django.urls import path
from . import views

urlpatterns = [

    # Projects homepage
    path(
        "",
        views.project_list,
        name="project_list"
    ),

    # Project detail
    path(
        "<slug:slug>/",
        views.project_detail,
        name="project_detail"
    ),

]