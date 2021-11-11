from .base import PostTestCase
from ..models import Post


class PostModelTestCase(PostTestCase):

    def test_post_string_is_title(self):
        """Posts are printed by their titles."""
        test_blog = Post.objects.get(title="My test blog")
        self.assertEqual(str(test_blog), "My test blog")
