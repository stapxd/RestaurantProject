from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='booking'),
    path('confirmation/', views.confirmation, name='confirmation'),
    path('profile/', views.profile, name='profile'),
]
