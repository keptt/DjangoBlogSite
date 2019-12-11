from django.urls import path
from . import views
from .views import PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView


urlpatterns = [
    path('', views.home, name='home-posts'),
    path('welcome/', views.welcome, name='welcome'),
    path('blog/', PostListView.as_view(), name='blog-posts'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='detail-posts'),
    path('post/<int:pk>/update', PostUpdateView.as_view(), name='update-posts'),
    path('post/<int:pk>/delete', PostDeleteView.as_view(), name='delete-posts'),
    path('post/new/', PostCreateView.as_view(), name='create-posts'),
]
