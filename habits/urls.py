from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('habit/add/', views.habit_add, name='habit-add'),
    path('habit/<int:pk>/delete/', views.habit_delete, name='habit-delete'),
    path('habit/<int:pk>/log/<str:date_str>/', views.log_toggle, name='log-toggle'),
    path('habit/<int:pk>/edit/', views.habit_edit, name='habit-edit'),
]
