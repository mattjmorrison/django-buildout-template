from django import http
from blog import models

def save(request):
    models.Blog.objects.create(name="matt", message="hey everybody")
    return http.HttpResponse("hi")
