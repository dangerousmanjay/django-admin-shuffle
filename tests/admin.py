from admin_shuffle import AdminShuffleMixin
from django.contrib import admin

from .models import Article


@admin.register(Article)
class ArticleAdmin(AdminShuffleMixin, admin.ModelAdmin):
    change_list_template = 'tests/change_list.html'
