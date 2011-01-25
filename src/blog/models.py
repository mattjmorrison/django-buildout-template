from django.db import models

class Blog(models.Model):
    message = models.CharField(max_length=128)