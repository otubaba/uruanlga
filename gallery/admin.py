from django.contrib import admin
from .models import Gallery, GalleryImage


class GalleryImageInline(admin.TabularInline):

    model = GalleryImage

    extra = 5


@admin.register(Gallery)
class GalleryAdmin(admin.ModelAdmin):

    prepopulated_fields = {
        'slug': ('title',)
    }

    inlines = [
        GalleryImageInline
    ]