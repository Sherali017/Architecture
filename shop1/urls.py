from django.urls import path

from shop1.views import ProductListView, ProductDetailView

app_name = 'shop1'
urlpatterns  = [
    path('', ProductListView.as_view(), name='list'),
    path('<int:pk>/', ProductDetailView.as_view(), name='detail')
]