from django.test import Client
from django.urls import reverse

from ..models import Project
from .base import ProjectTestCase


class ProjectFormTestCase(ProjectTestCase):
    def test_projects_form_response(self):
        """Projects form urls redirect when user is not logged in."""
        test_project = Project.objects.get(title="My test project")
        client = Client()
        update_response = client.get(
            reverse("projects:update", kwargs={"pk": test_project.id})
        )
        self.assertRedirects(
            update_response,
            reverse("account_login")
            + "?next="
            + reverse("projects:update", kwargs={"pk": test_project.id}),
        )

        create_response = client.get(reverse("projects:create"))
        self.assertRedirects(
            create_response,
            reverse("account_login") + "?next=" + reverse("projects:create"),
        )

    def test_create_form_submit(self):
        """Project create form submits normally."""
        client = Client()
        client.login(username="testuser", password="12345")
        url = reverse("projects:create")
        form_response = client.post(
            path=url,
            data={
                "title": "new project",
                "tag_line": "some project tag line",
                "body": "<p>Body Text</p>",
                "is_published": True,
                "header_image": self.image,
            },
        )
        self.assertEqual(form_response.status_code, 200)

    def test_update_form_submit(self):
        """Project update form submits normally."""
        test_project = Project.objects.get(title="My test project")
        client = Client()
        client.login(username="testuser", password="12345")
        url = reverse("projects:update", kwargs={"pk": test_project.id})
        form_response = client.post(
            path=url,
            data={
                "title": test_project.title,
                "tag_line": test_project.tag_line,
                "body": test_project.body,
                "is_published": test_project.is_published,
                "header_image": self.image,
            },
        )
        self.assertEqual(form_response.status_code, 200)
