from django import http

from blog.models import Blog

def index(request):
    return http.HttpResponse("<h1>Hello World</h1> <div>%s</div>" % Blog.objects.all())
