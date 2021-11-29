from django.contrib import admin

from about.models import AboutModel, FeaturesModel, ClientModel, ProcessModel, VideoModel


@admin.register(AboutModel)
class AboutModelAdmin(admin.ModelAdmin):
    list_display = ['title', 'content', 'created_at']
    list_filter = ['created_at']
    search_fields = ['title', 'content', 'created_at']


@admin.register(FeaturesModel)
class FeaturesModelAdmin(admin.ModelAdmin):
    list_display = ['title', 'long_text', 'created_at']
    list_filter = ['created_at']
    search_fields = ['title', 'long_text', 'created_at']

@admin.register(ClientModel)
class ClientModelAdmin(admin.ModelAdmin):
    list_display = ['name', 'content', 'created_at']
    list_filter = ['created_at']
    search_fields = ['created_at']

@admin.register(ProcessModel)
class ProcessModelAdmin(admin.ModelAdmin):
    list_display = ['number', 'title', 'long_desc', 'created_at']
    list_filter = ['created_at']
    search_fields = ['number', 'title' 'long_desc']

@admin.register(VideoModel)
class VideoModelAdmin(admin.ModelAdmin):
    list_display = ['title', 'suggestion', 'about_video', 'created_at']
    list_filter = ['created_at']
    search_fields = ['title', 'created_at']


