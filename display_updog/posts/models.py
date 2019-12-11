from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.

# class Page(models.Model):
#     pagename = models.CharField(max_length=100)


# class Content(models.Model):
#     text = models.TextField() 
#     desc = models.CharField(max_length=100)
#     order = models.IntegerField()
#     page = models.ForeignKey(Page, on_delete=models.PROTECT)

class Post(models.Model):
    title       = models.CharField(max_length=100)
    content     = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author      = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('detail-posts', kwargs={'pk': self.pk})
