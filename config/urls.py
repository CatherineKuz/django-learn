from django.contrib import admin
from django.urls import path, include
from habits import views as habits_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/register/', habits_views.register, name='register'),
    path('', include('habits.urls')),
]