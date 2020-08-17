from admin_shuffle import AdminShuffleMixin
from django.contrib import admin

from .models import Article


@admin.register(Article)
class ArticleAdmin(AdminShuffleMixin, admin.ModelAdmin):
    list_display = (
        'title',
        'content',
        'created_at',
    )
