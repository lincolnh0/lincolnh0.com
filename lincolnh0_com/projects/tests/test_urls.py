from django.urls import resolve, reverse
from .base import ProjectTestCase
from ..models import Project


class ProjectUrlTestCase(ProjectTestCase):

    def test_project_url(self):
        """Projects urls are correctly generated."""
        test_project = Project.objects.get(title="My test project")
        self.assertEqual(test_project.get_absolute_url(), reverse("projects:detail", kwargs={"slug": test_project.slug}))
        self.assertEqual(resolve(test_project.get_absolute_url()).view_name, "projects:detail")


