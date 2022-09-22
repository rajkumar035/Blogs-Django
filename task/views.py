from operator import truediv
from django.shortcuts import render
from .models import Post
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import (
    ListView, #Show all our posts in list view to manage(ordering, rendering, etc...)
    DetailView, #detail view is for showing the post with that same data detailed in another page
    CreateView, #It is for creating a new list of data like in the prototype
    UpdateView ) #It is for updating/editing the post

def first(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'task/home.html', context) #3rd attribute is for sending some data it acts like an props

class PostListView(ListView):
    model = Post #Assigning the Post(from model) to view in list view
    template_name = 'task/home.html' #For assigning the data should be displayed in this template to view
    context_object_name = 'posts' #Sending the object of datas using this line

class PostDetailView(DetailView):
    model = Post

class PostCreateView(LoginRequiredMixin, CreateView): # LoginRequiredMixin sets our application to only create post when user logged in and another argument called create view is for passing that this data should be managed by this method
    model = Post
    fields = ['name', 'password', 'dob']
    def form_valid(self, form):
        form.instance.client = self.request.user
        return super().form_valid(form)

class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView): # UserPassesTestMixin it is for that we saying that that the client of the post should only update and another argument called update view is for updating the data of the selected post
    model = Post
    fields = ['name', 'password', 'dob']
    def form_valid(self, form):
        form.instance.client = self.request.user
        return super().form_valid(form)
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.client:
            return True
        else:
            return False

def about(request):
    return render(request, 'task/about.html', {'title': 'About'})