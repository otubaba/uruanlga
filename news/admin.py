from django.contrib import admin
from .models import Category, News, BreakingNews

admin.site.register(Category)
admin.site.register(News)


@admin.register(BreakingNews)
class BreakingNewsAdmin(admin.ModelAdmin):
    list_display = ('title', 'active')
    list_filter = ('active',)
    search_fields = ('title',)