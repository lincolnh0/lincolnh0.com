from django.urls import resolve, reverse
from django.test import Client
from .base import ProjectTestCase
from ..models import Project


class ProjectUrlTestCase(ProjectTestCase):
    def test_projects_url(self):
        """Projects urls are correctly generated."""
        test_project = Project.objects.get(title="My test project")
        self.assertEqual(
            test_project.get_absolute_url(),
            reverse("projects:detail", kwargs={"slug": test_project.slug}),
        )
        self.assertEqual(
            resolve(test_project.get_absolute_url()).view_name, "projects:detail"
        )

        # Check when project title is changed, slug is updated.
        test_project.title = "My updated project title"
        test_project.save()

        self.assertEqual(
            test_project.get_absolute_url(),
            reverse("projects:detail", kwargs={"slug": test_project.slug}),
        )
        self.assertEqual(
            resolve(test_project.get_absolute_url()).view_name, "projects:detail"
        )

    def test_projects_url_response(self):
        """Projects urls return correct status code."""
        test_project = Project.objects.get(title="My test project")
        client = Client()
        detail_response = client.get(
            reverse("projects:detail", kwargs={"slug": test_project.slug})
        )
        self.assertEqual(detail_response.status_code, 200)

        list_response = client.get(reverse("projects:list"))
        self.assertEqual(list_response.status_code, 200)
