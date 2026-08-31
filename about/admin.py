from django.contrib import admin
from .models import AboutSection
from .models import HomeHero

@admin.register(AboutSection)
class AboutSectionAdmin(admin.ModelAdmin):

    list_display = (
        'title',
        'slug',
        'created_at',
        'updated_at'
    )

    search_fields = (
        'title',
        'content'
    )

    prepopulated_fields = {
        'slug': ('title',)
    }

    list_filter = (
        'created_at',
        'updated_at'
    )

from django.contrib import admin
from .models import ProminentIndigene


@admin.register(ProminentIndigene)
class ProminentIndigeneAdmin(admin.ModelAdmin):

    list_display = (
        "name",
        "title",
        "profession",
        "community",
        "featured",
        "order",
    )

    list_filter = (
        "featured",
        "profession",
        "community",
    )

    search_fields = (
        "name",
        "profession",
        "position",
        "community",
        "clan",
        "ward",
    )

    prepopulated_fields = {
        "slug": ("name",)
    }

    list_editable = (
        "featured",
        "order",
    )

@admin.register(HomeHero)
class HomeHeroAdmin(admin.ModelAdmin):

    list_display = (
        "heading",
        "highlighted_text",
        "is_active",
        "updated_at",
    )

    list_filter = (
        "is_active",
    )

    search_fields = (
        "heading",
        "highlighted_text",
        "description",
    )

    readonly_fields = (
        "created_at",
        "updated_at",
    )

    fieldsets = (

        (
            "Hero Content",
            {
                "fields": (
                    "background_image",
                    "heading",
                    "highlighted_text",
                    "heading_suffix",
                    "description",
                )
            }
        ),

        (
            "Primary Button",
            {
                "fields": (
                    "primary_button_text",
                    "primary_button_url",
                )
            }
        ),

        (
            "Secondary Button",
            {
                "fields": (
                    "secondary_button_text",
                    "secondary_button_url",
                )
            }
        ),

        (
            "Homepage Statistics",
            {
                "fields": (
                    "population",
                    "population_label",
                    "communities",
                    "communities_label",
                    "schools",
                    "schools_label",
                    "health_centres",
                    "health_centres_label",
                    "markets",
                    "markets_label",
                    "projects",
                    "projects_label",
                )
            }
        ),

        (
            "Status",
            {
                "fields": (
                    "is_active",
                    "created_at",
                    "updated_at",
                )
            }
        ),

    )

