from django.urls import path
from . import views

urlpatterns = [
    path('', views.first, name='task-first'),
    path('about/', views.about, name='task-about')
]