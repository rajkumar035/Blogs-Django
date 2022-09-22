from django.urls import path
from . import views
from .views import PostListView, PostDetailView, PostCreateView, PostUpdateView

urlpatterns = [
    path('', PostListView.as_view(), name='task-first'), #as_view() is for assigning the list to render/perform in the view page format
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-det'), #It was like an dynamic url <int:pk> returns the primary key of the post
    path('post/new/', PostCreateView.as_view(), name='post-create'), 
    path('post/<int:pk>/edit', PostUpdateView.as_view(), name='post-edit'),
    path('about/', views.about, name='task-about')
]