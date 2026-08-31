from django.contrib import admin
from django.utils.html import format_html

from .models import (
    ClanCategory,
    Clan,
    Ward,
    Village,
)


# ============================================================
# CLAN CATEGORY ADMIN
# ============================================================

@admin.register(ClanCategory)
class ClanCategoryAdmin(admin.ModelAdmin):

    list_display = (
        "name",
        "slug",
        "clan_count",
        "created_at",
    )

    list_filter = (
        "name",
        "created_at",
    )

    search_fields = (
        "name",
        "description",
        "slug",
    )

    prepopulated_fields = {
        "slug": ("name",),
    }

    readonly_fields = (
        "created_at",
        "image_preview",
    )

    fieldsets = (
        (
            "Category Information",
            {
                "fields": (
                    "name",
                    "slug",
                    "description",
                    "image",
                    "image_preview",
                )
            },
        ),
        (
            "System Information",
            {
                "fields": (
                    "created_at",
                )
            },
        ),
    )

    def clan_count(self, obj):
        return obj.clans.count()

    clan_count.short_description = "Clans"

    def image_preview(self, obj):
        if obj.image:
            return format_html(
                '<img src="{}" width="120" height="80" '
                'style="object-fit:cover;border-radius:8px;" />',
                obj.image.url,
            )

        return "No image"

    image_preview.short_description = "Preview"


# ============================================================
# CLAN ADMIN
# ============================================================

@admin.register(Clan)
class ClanAdmin(admin.ModelAdmin):

    list_display = (
        "name",
        "category",
        "ward_count",
        "image_preview",
        "created_at",
    )

    list_filter = (
        "category",
        "created_at",
    )

    search_fields = (
        "name",
        "slug",
        "description",
        "category__name",
    )

    prepopulated_fields = {
        "slug": ("name",),
    }

    autocomplete_fields = (
        "category",
    )

    readonly_fields = (
        "created_at",
        "image_preview",
    )

    fieldsets = (
        (
            "Clan Information",
            {
                "fields": (
                    "category",
                    "name",
                    "slug",
                    "description",
                    "image",
                    "image_preview",
                )
            },
        ),
        (
            "System Information",
            {
                "fields": (
                    "created_at",
                )
            },
        ),
    )

    def ward_count(self, obj):
        return obj.wards.count()

    ward_count.short_description = "Wards"

    def image_preview(self, obj):
        if obj.image:
            return format_html(
                '<img src="{}" width="120" height="80" '
                'style="object-fit:cover;border-radius:8px;" />',
                obj.image.url,
            )

        return "No image"

    image_preview.short_description = "Preview"


# ============================================================
# WARD ADMIN
# ============================================================

@admin.register(Ward)
class WardAdmin(admin.ModelAdmin):

    list_display = (
        "name",
        "clan",
        "category",
        "village_count",
        "created_at",
    )

    list_filter = (
        "clan__category",
        "clan",
        "created_at",
    )

    search_fields = (
        "name",
        "slug",
        "description",
        "clan__name",
        "clan__category__name",
    )

    prepopulated_fields = {
        "slug": ("name",),
    }

    autocomplete_fields = (
        "clan",
    )

    readonly_fields = (
        "created_at",
    )

    fieldsets = (
        (
            "Ward Information",
            {
                "fields": (
                    "clan",
                    "name",
                    "slug",
                    "description",
                )
            },
        ),
        (
            "System Information",
            {
                "fields": (
                    "created_at",
                )
            },
        ),
    )

    def category(self, obj):
        return obj.clan.category.get_name_display()

    category.short_description = "Category"

    def village_count(self, obj):
        return obj.villages.count()

    village_count.short_description = "Villages"


# ============================================================
# VILLAGE ADMIN
# ============================================================

@admin.register(Village)
class VillageAdmin(admin.ModelAdmin):

    list_display = (
        "name",
        "ward",
        "clan",
        "category",
        "village_head",
        "population",
        "image_preview",
        "created_at",
    )

    list_filter = (
        "ward__clan__category",
        "ward__clan",
        "ward",
        "created_at",
    )

    search_fields = (
        "name",
        "slug",
        "village_head",
        "description",
        "history",
        "ward__name",
        "ward__clan__name",
        "ward__clan__category__name",
    )

    prepopulated_fields = {
        "slug": ("name",),
    }

    autocomplete_fields = (
        "ward",
    )

    readonly_fields = (
        "created_at",
        "updated_at",
        "image_preview",
    )

    fieldsets = (
        (
            "Village Information",
            {
                "fields": (
                    "ward",
                    "name",
                    "slug",
                    "image",
                    "image_preview",
                )
            },
        ),
        (
            "Leadership & Population",
            {
                "fields": (
                    "village_head",
                    "population",
                )
            },
        ),
        (
            "History & Description",
            {
                "fields": (
                    "history",
                    "description",
                )
            },
        ),
        (
            "Location",
            {
                "fields": (
                    "latitude",
                    "longitude",
                )
            },
        ),
        (
            "System Information",
            {
                "fields": (
                    "created_at",
                    "updated_at",
                )
            },
        ),
    )

    def clan(self, obj):
        return obj.ward.clan.name

    clan.short_description = "Clan"

    def category(self, obj):
        return obj.ward.clan.category.get_name_display()

    category.short_description = "Category"

    def image_preview(self, obj):
        if obj.image:
            return format_html(
                '<img src="{}" width="140" height="90" '
                'style="object-fit:cover;border-radius:8px;" />',
                obj.image.url,
            )

        return "No image"

    image_preview.short_description = "Preview"