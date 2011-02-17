from django.db import models

class BlogManager(models.Manager):
    pass

class Blog(models.Model):
    name = models.CharField(max_length=20)
    message = models.CharField(max_length=200)

    objects = BlogManager()