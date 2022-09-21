from django.shortcuts import render
from .models import Post
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import (
    ListView, #Show all our posts in list view to manage(ordering, rendering, etc...)
    DetailView, #detail view is for showing the post with that same data detailed in another page
    CreateView ) #It is for

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

class PostCreateView(LoginRequiredMixin, CreateView): # LoginRequiredMixin sets our application to only create post when user logged in
    model = Post
    fields = ['name', 'password', 'dob']
    def form_valid(self, form):
        form.instance.client = self.request.user
        return super().form_valid(form)

def about(request):
    return render(request, 'task/about.html', {'title': 'About'})