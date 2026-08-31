from django.contrib import admin

from .models import CouncilLeadership, PastChairman


@admin.register(CouncilLeadership)
class CouncilLeadershipAdmin(admin.ModelAdmin):

    list_display = (
        "full_name",
        "council_type",
        "designation",
        "ward",
        "current",
        "featured",
        "show_on_homepage",
        "show_chairman_message",
        "order",
    )

    list_filter = (
        "council_type",
        "current",
        "featured",
        "show_on_homepage",
        "show_chairman_message",
    )

    search_fields = (
        "full_name",
        "designation",
        "ward",
        "community",
        "political_party",
        "profession",
    )

    prepopulated_fields = {
        "slug": ("full_name",)
    }

    list_editable = (
        "featured",
        "show_on_homepage",
        "show_chairman_message",
        "order",
    )

    ordering = (
        "council_type",
        "order",
        "full_name",
    )

    fieldsets = (

        # ======================================================
        # PERSONAL INFORMATION
        # ======================================================

        (
            "Personal Information",
            {
                "fields": (
                    "full_name",
                    "slug",
                    "title",
                    "photo",
                    "date_of_birth",
                    "profession",
                    "qualification",
                )
            }
        ),

        # ======================================================
        # COUNCIL POSITION
        # ======================================================

        (
            "Council Position",
            {
                "fields": (
                    "council_type",
                    "designation",
                    "custom_designation",
                    "ward",
                    "community",
                    "political_party",
                )
            }
        ),

        # ======================================================
        # BIOGRAPHY
        # ======================================================

        (
            "Biography & Achievements",
            {
                "fields": (
                    "biography",
                    "achievements",
                )
            }
        ),

        # ======================================================
        # CHAIRMAN'S MESSAGE
        # ======================================================

        (
            "Chairman's Message",
            {
                "fields": (
                    "message_title",
                    "chairman_message",
                    "show_chairman_message",
                ),

                "description": (
                    "Complete this section for the Executive Chairman "
                    "whose official message should appear on the website."
                ),
            }
        ),

        # ======================================================
        # TENURE
        # ======================================================

        (
            "Tenure",
            {
                "fields": (
                    "date_assumed_office",
                    "date_left_office",
                    "current",
                )
            }
        ),

        # ======================================================
        # CONTACT INFORMATION
        # ======================================================

        (
            "Contact Information",
            {
                "fields": (
                    "email",
                    "phone",
                    "office_address",
                )
            }
        ),

        # ======================================================
        # WEBSITE DISPLAY
        # ======================================================

        (
            "Website Display",
            {
                "fields": (
                    "featured",
                    "show_on_homepage",
                    "order",
                )
            }
        ),
    )


from django.contrib import admin
from .models import TraditionalLeader


@admin.register(TraditionalLeader)
class TraditionalLeaderAdmin(admin.ModelAdmin):

    list_display = (
        "full_name",
        "display_designation",
        "leadership_type",
        "community",
        "current",
        "featured",
        "order",
    )

    list_filter = (
        "leadership_type",
        "current",
        "featured",
        "show_on_homepage",
    )

    search_fields = (
        "full_name",
        "traditional_title",
        "custom_designation",
        "clan",
        "ward",
        "community",
        "village",
    )

    prepopulated_fields = {
        "slug": ("full_name",)
    }

    ordering = (
        "-current",
        "order",
        "full_name",
    )

@admin.register(PastChairman)
class PastChairmanAdmin(admin.ModelAdmin):

    list_display = (
        "full_name",
        "tenure_display",
        "profession",
        "featured",
        "order",
    )

    list_filter = (
        "featured",
    )

    search_fields = (
        "full_name",
        "profession",
        "community",
        "clan",
        "achievements",
    )

    prepopulated_fields = {
        "slug": ("full_name",)
    }

    list_editable = (
        "featured",
        "order",
    )

    ordering = (
        "-tenure_end",
        "order",
        "full_name",
    )

    fieldsets = (

        (
            "Personal Information",
            {
                "fields": (
                    "full_name",
                    "slug",
                    "title",
                    "photo",
                    "profession",
                    "qualification",
                    "community",
                    "clan",
                )
            }
        ),

        (
            "Tenure",
            {
                "fields": (
                    "tenure_start",
                    "tenure_end",
                    "tenure_description",
                )
            }
        ),

        (
            "Biography",
            {
                "fields": (
                    "biography",
                )
            }
        ),

        (
            "Administration & Service",
            {
                "fields": (
                    "service_summary",
                    "achievements",
                    "major_projects",
                    "challenges",
                    "legacy",
                )
            }
        ),

        (
            "Recognition",
            {
                "fields": (
                    "awards",
                )
            }
        ),

        (
            "Website Display",
            {
                "fields": (
                    "featured",
                    "order",
                )
            }
        ),
    )

    @admin.display(
        description="Tenure",
        ordering="tenure_end"
    )
    def tenure_display(self, obj):

        return obj.tenure