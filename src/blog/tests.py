import mock
from django.core.urlresolvers import reverse
from django import test
from blog import models

@mock.patch('blog.models.Blog.objects', mock.Mock())
class BlogTests(test.TestCase):

    def test_creates_new_blog(self):
        self.client.get(reverse('blog:save'), {})
        self.assertEqual(((), {'name':'matt', 'message':"hey everybody"}),
                         models.Blog.objects.create.call_args)
