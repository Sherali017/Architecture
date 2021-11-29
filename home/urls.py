from django.urls import path

from home.views import HomeView, ServiceDetailView

app_name = 'home'
urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('detail/<int:pk>service/', ServiceDetailView.as_view(), name='service')
]