from django.conf.urls.defaults import *

urlpatterns = patterns('blog.views',
    url(r'^$', 'save', name='save'),
)

