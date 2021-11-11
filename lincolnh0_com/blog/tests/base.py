from django.test import TestCase
from ..models import Post


class PostTestCase(TestCase):
    def setUp(self):
        Post.objects.create(
            title="My test blog",
            body="<p>Test content</p>",
            is_published=False
        )
        Post.objects.create(
            title="My published test blog",
            body="<p>Test content</p>",
            is_published=True
        )
