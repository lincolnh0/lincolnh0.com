from django.test import TestCase
from lincolnh0_com.users.models import User
from ..models import Post


class PostTestCase(TestCase):
    def setUp(self):
        Post.objects.create(
            title="My test blog", body="<p>Test content</p>", is_published=False
        )
        Post.objects.create(
            title="My published test blog",
            body="<p>Test content</p>",
            is_published=True,
        )

        self.user = User.objects.create(username="testuser")
        self.user.set_password("12345")
        self.user.save()
