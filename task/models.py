from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

class Post(models.Model):
    name = models.CharField(max_length=100)
    password = models.IntegerField()
    dob = models.DateField()
    client = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    def get_absolute_url(self): #for redirecting to the mentioned path the recently created data
        return reverse('post-det', kwargs={'pk': self.pk})