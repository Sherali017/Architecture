from django.urls import path

from projects.views import ProjectView, ProjectDetailView

app_name = 'projects'
urlpatterns = [
    path('', ProjectView.as_view(), name='project'),
    path('<int:pk>/', ProjectDetailView.as_view(), name='detail')
]