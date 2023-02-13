from django.db import models
from django.contrib.auth.models import User
from django.shortcuts import reverse
from datetime import datetime, date

# Category 
class Category(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('home')

# Posts 
class Post(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    category = models.CharField(max_length=200, default='default')
    likes = models.ManyToManyField(User, related_name='blog_post')

    def __str__(self):
        return self.title + str(self.author)

    def get_absolute_url(self):
        return reverse('home')