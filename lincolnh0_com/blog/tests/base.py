from django.test import TestCase
from ..models import Blog


class BlogTestCase(TestCase):
    def setUp(self):
        Blog.objects.create(
            title="My test blog",
            body="<p>Test content</p>",
            is_published=False
        )
        Blog.objects.create(
            title="My published test blog",
            body="<p>Test content</p>",
            is_published=True
        )
