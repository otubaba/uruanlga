from django.urls import path
from . import views




urlpatterns = [

    # ==========================================================
    # PAST CHAIRMEN
    # ==========================================================

    path(
        "chairmen/",
        views.past_chairman_list,
        name="past_chairman_list",
    ),

    path(
        "chairmen/<int:pk>/",
        views.past_chairman_detail,
        name="past_chairman_detail",
    ),

    path(
        "chairman-message/",
        views.chairman_message,
        name="chairman_message",
    ),


    # ==========================================================
    # EXECUTIVE LEADERSHIP
    # ==========================================================

    path(
        "government/executive/",
        views.executive_leadership,
        name="executive_leadership",
    ),

    path(
        "government/executive/<slug:slug>/",
        views.executive_leadership_detail,
        name="executive_leadership_detail",
    ),


    # ==========================================================
    # LEGISLATIVE LEADERSHIP
    # ==========================================================

    path(
        "government/legislative/",
        views.legislative_leadership,
        name="legislative_leadership",
    ),

    path(
        "government/legislative/<slug:slug>/",
        views.legislative_leadership_detail,
        name="legislative_leadership_detail",
    ),


    # ==========================================================
    # TRADITIONAL LEADERSHIP
    # ==========================================================

    path(
        "traditional-leaders/",
        views.traditional_leader_list,
        name="traditional_leadership",
    ),

    path(
        "traditional-leaders/<slug:slug>/",
        views.traditional_leader_detail,
        name="traditional_leadership_detail",
    ),

]