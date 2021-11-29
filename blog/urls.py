from django.urls import path

from blog.views import Blogview, BlogDetailView, CommentCreateView


app_name='blog'
urlpatterns = [
    path('', Blogview.as_view(), name='view' ),
    path('detail/<int:pk>/', CommentCreateView.as_view(), name='comment' ),
    path('detail/<int:pk>comment/', BlogDetailView.as_view(), name='detail'),

]