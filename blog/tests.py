from django.test import TestCase
from .models import Blog

class BlogTestCase(TestCase):
    def setUp(self):
        Blog.objects.create(name='Teste', status=1, validate='2025-12-31')

    def test_blog_created(self):
        blog = Blog.objects.get(name='Teste')
        self.assertEqual(blog.status, 1)
