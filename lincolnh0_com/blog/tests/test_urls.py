from django.urls import resolve, reverse
from .base import BlogTestCase
from ..models import Blog


class BlogUrlTestCase(BlogTestCase):

    def test_blog_url(self):
        """Blogs urls are correctly generated."""
        test_blog = Blog.objects.get(title="My test blog")
        self.assertEqual(test_blog.get_absolute_url(), reverse("blog:detail", kwargs={"slug": test_blog.slug}))
        self.assertEqual(resolve(test_blog.get_absolute_url()).view_name, "blog:detail")


