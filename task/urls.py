from django.urls import path
from . import views
from .views import PostListView, PostDetailView, PostCreateView

urlpatterns = [
    path('', PostListView.as_view(), name='task-first'), #as_view() is for assigning the list to render/perform in the view page format
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-det'), #It was like an dynamic url <int:pk> returns the primary key of the post
    path('post/new/', PostCreateView.as_view(), name='post-create'), #It was like an dynamic url <int:pk> returns the primary key of the post
    path('about/', views.about, name='task-about')
]