from django.contrib import admin


from projects.models import CategoryModel, projectModel


@admin.register(CategoryModel)
class CategoryModelAdmin(admin.ModelAdmin):
    list_display = ['title']
    list_filter = ['title']
    search_fields = ['title']

@admin.register(projectModel)
class projectModelAdmin(admin.ModelAdmin):
    list_display = ['name', 'title', 'created_at']
    list_filter = ['created_at']
    search_fields = ['name', 'title', 'created_at']
