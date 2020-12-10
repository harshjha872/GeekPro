from django.db import models
from django.utils import timezone
from django.urls import reverse
from django.contrib.auth.models import User
# Create your models here.

class Article(models.Model):
    title=models.CharField(max_length=80)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default2.jpg', upload_to='article_pics')
    content=models.TextField()
    date_added=models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('home')

class Contact(models.Model):
    name=models.CharField(max_length=50)
    email=models.EmailField()
    subject=models.CharField(max_length=80)
    message=models.TextField()

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('home')