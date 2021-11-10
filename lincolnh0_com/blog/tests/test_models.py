from .base import BlogTestCase
from ..models import Blog


class BlogModelTestCase(BlogTestCase):

    def test_project_string_is_title(self):
        """Projects are printed by their titles."""
        test_project = Blog.objects.get(title="My test blog")
        self.assertEqual(str(test_project), "My test blog")
