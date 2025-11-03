from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),

    # API endpoints (return JSON)
    path('api/posts/', views.api_post_list, name='api_post_list'),
    path('api/posts/<int:pk>/', views.api_post_detail, name='api_post_details'),
]
