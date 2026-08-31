from django.urls import path
from . import views




urlpatterns = [

    # ============================================================
    # CLAN CATEGORIES
    # ============================================================

    path(
        "",
        views.clan_category_list,
        name="clan_category_list"
    ),

    path(
        "category/<slug:slug>/",
        views.clan_category_detail,
        name="clan_category_detail"
    ),


    # ============================================================
    # CLANS
    # ============================================================

    path(
        "clan/list/",
        views.clan_list,
        name="clan_list"
    ),

    path(
        "clan/<slug:slug>/",
        views.clan_detail,
        name="clan_detail"
    ),


    # ============================================================
    # WARDS
    # ============================================================

    path(
        "clan/<slug:clan_slug>/ward/<slug:slug>/",
        views.ward_detail,
        name="ward_detail"
    ),


    # ============================================================
    # VILLAGES
    # ============================================================

    path(
        "ward/<slug:ward_slug>/village/<slug:slug>/",
        views.village_detail,
        name="village_detail"
    ),

]