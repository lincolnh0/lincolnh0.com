from ..models import Project
from .base import ProjectTestCase


class ProjectModelTestCase(ProjectTestCase):
    def test_project_string_is_title(self):
        """Projects are printed by their titles."""
        test_project = Project.objects.get(title="My test project")
        self.assertEqual(str(test_project), "My test project")
