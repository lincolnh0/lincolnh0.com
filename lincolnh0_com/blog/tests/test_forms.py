from django.test import Client
from django.urls import reverse

from ..models import Post
from .base import PostTestCase


class PostFormTestCase(PostTestCase):
    def test_posts_form_response(self):
        """Posts form urls redirect when user is not logged in."""
        test_post = Post.objects.get(title="My test blog")
        client = Client()
        update_response = client.get(
            reverse("blog:update", kwargs={"pk": test_post.id})
        )
        self.assertRedirects(
            update_response,
            reverse("account_login")
            + "?next="
            + reverse("blog:update", kwargs={"pk": test_post.id}),
        )

        create_response = client.get(reverse("blog:create"))
        self.assertRedirects(
            create_response,
            reverse("account_login") + "?next=" + reverse("blog:create"),
        )

    def test_create_form_submit(self):
        """Post create form submits normally."""
        client = Client()
        client.force_login(self.user, backend=None)
        url = reverse("blog:create")
        form_response = client.post(
            path=url,
            data={
                "title": "new project",
                "body": "<p>Body Text</p>",
                "is_published": True,
            },
        )
        self.assertRedirects(
            form_response,
            expected_url=reverse(
                "blog:detail",
                kwargs={
                    "slug": "new-project",
                },
            ),
        )

    def test_update_form_submit(self):
        """Post update form submits normally."""
        test_post = Post.objects.get(title="My test blog")
        client = Client()
        client.login(username="testuser", password="12345")
        url = reverse("blog:update", kwargs={"pk": test_post.id})
        form_response = client.post(
            path=url,
            data={
                "title": test_post.title,
                "body": test_post.body,
                "is_published": test_post.is_published,
            },
        )
        self.assertRedirects(
            form_response,
            expected_url=reverse(
                "blog:detail",
                kwargs={
                    "slug": test_post.slug,
                },
            ),
        )
