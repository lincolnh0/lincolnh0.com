from django.urls import resolve, reverse

from ..models import Post
from .base import PostTestCase


class PostUrlTestCase(PostTestCase):
    def test_post_url(self):
        """Blogs urls are correctly generated."""
        test_blog = Post.objects.get(title="My test blog")
        self.assertEqual(
            test_blog.get_absolute_url(),
            reverse("blog:detail", kwargs={"slug": test_blog.slug}),
        )
        self.assertEqual(resolve(test_blog.get_absolute_url()).view_name, "blog:detail")
