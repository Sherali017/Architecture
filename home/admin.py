from django.contrib import admin

from home.models import SpecializationModel, projectsModel, TeamModel, ClientsModel, NewsModel, PartnerModel


@admin.register(SpecializationModel)
class SpecializationModelAdmin(admin.ModelAdmin):
    list_display = ['title', 'description', 'created_at']
    list_filter = ['created_at']
    search_fields = ['title', 'description', 'created_at']





@admin.register(projectsModel)
class projectsModelAdmin(admin.ModelAdmin):
    list_display = ['title', 'type', 'created_at']
    list_filter = ['created_at']
    search_fields = ['title', 'type', 'created_at']


@admin.register(TeamModel)
class TeamModelAdmin(admin.ModelAdmin):
    list_display = ['name', 'job', 'created_at']
    list_filter = ['created_at']
    search_fields = ['name', 'job', 'created_at']


@admin.register(ClientsModel)
class  ClientsModeAdmin(admin.ModelAdmin):
    list_display = ['name', 'job', 'created_at']
    list_filter = ['created_at']
    search_fields = ['name', 'job']


@admin.register(NewsModel)
class NewsModelAdmin(admin.ModelAdmin):
    list_display = ['title', 'post_by', 'created_at']
    list_filter = ['created_at']
    search_fields = ['title', 'post_by', 'created_at']


@admin.register(PartnerModel)
class PartnerModelAdmin(admin.ModelAdmin):
    list_display = ['created_at']
    search_fields = ['created_at']


