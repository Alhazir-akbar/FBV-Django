from django.urls import path, re_path
from . import views

app_name = 'blog'

urlpatterns = [
    path('delete/<int:delete_id>/', views.delete, name='delete'),
    path('update/<int:update_id>/', views.update, name='update'),
    path('create/', views.create, name='create'),
    path('', views.list, name='list'),
]