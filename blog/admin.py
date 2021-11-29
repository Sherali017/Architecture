from django.contrib import admin

from blog.models import AuthorModel, PostTagModel, PostModel, CommentModel


@admin.register(AuthorModel)
class AuthorModelAdmin(admin.ModelAdmin):
    list_display = ['name', 'created_at', 'title']
    list_filter = ['created_at']
    search_fields = ['name', 'title']

@admin.register(PostTagModel)
class PostTagModelAdmin(admin.ModelAdmin):
    list_display = ['title', 'created_at']
    list_filter = ['created_at']
    search_fields = ['title']

@admin.register(PostModel)
class PostModelAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'created_at']
    list_filter = ['author', 'tags', 'created_at']
    search_fields = ['title']
    autocomplete_fields = ['author', 'tags']

@admin.register(CommentModel)
class CommentModelAdmin(admin.ModelAdmin):
    list_display = ['post', 'name', 'email', 'phone', 'created_at']
    list_filter = ['created_at']
    search_fields = ['name', 'email']


# @admin.register(CategoryModel)
# class CategoryModelAdmin(admin.ModelAdmin):
#     list_display = ['title']
#     list_filter = ['created_at']
#     search_fields = ['title']





