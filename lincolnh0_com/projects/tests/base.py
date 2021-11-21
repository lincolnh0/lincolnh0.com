from django.test import TestCase
from ..models import Project


class ProjectTestCase(TestCase):
    def setUp(self):
        Project.objects.create(
            title="My test project",
            tag_line="There is only this many tag line",
            body="<p>Test content</p>",
            is_published=False,
        )
        Project.objects.create(
            title="My published test project",
            tag_line="There is only this many tag line",
            body="<p>Test content</p>",
            is_published=True,
        )
