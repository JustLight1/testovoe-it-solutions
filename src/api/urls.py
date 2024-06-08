from django.urls import path

from .views import PostsList, PostDetail


urlpatterns = [
    path('posts/', PostsList.as_view(), name='post-list'),
    path('post/<int:id>/', PostDetail.as_view(), name='post-detail'),
]
