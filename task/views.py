from multiprocessing import context
from django.shortcuts import render
from .models import Post

posts = [
    {
        "username": "Rajkumar",
        "DOB": "03-05-2004",
        "Password" : "03052004",
    },
        {
        "username": "Prem Kumar",
        "DOB": "02-04-1993",
        "Password" : "23041994",
    },
        {
        "username": "Nishanth",
        "DOB": "10-08-1995",
        "Password" : "08081995",
    }
]

def first(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'task/home.html', context)

def about(request):
    return render(request, 'task/about.html', {'title': 'About'})