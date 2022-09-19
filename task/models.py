from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):
    name = models.CharField(max_length=100)
    password = models.TextField(max_length=10)
    dob = models.DateField()
    client = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name