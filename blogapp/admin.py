from django.contrib import admin
from blogapp.models import Category, Article, Comment


class ArticleAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "author")


class CategoryAdmin(admin.ModelAdmin):
    list_display = ("id", "name")


class CommentAdmin(admin.ModelAdmin):
    list_display = ("article", "author", "content")


admin.site.register(Article, ArticleAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Comment, CommentAdmin)
