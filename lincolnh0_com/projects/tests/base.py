from os.path import dirname, join
from django.test import TestCase
from django.core.files.uploadedfile import SimpleUploadedFile
from lincolnh0_com.users.models import User
from ..models import Project


class ProjectTestCase(TestCase):
    def setUp(self):
        base_dir = dirname(dirname(dirname(__file__)))
        self.image = SimpleUploadedFile(
            name="test_image.jpg",
            content=open(join(base_dir, "static/tests/test_image.jpg"), "rb").read(),
            content_type="image/jpeg",
        )
        Project.objects.create(
            title="My test project",
            tag_line="There is only this many tag line",
            body="<p>Test content</p>",
            is_published=False,
            header_image=self.image,
        )
        Project.objects.create(
            title="My published test project",
            tag_line="There is only this many tag line",
            body="<p>Test content</p>",
            is_published=True,
            header_image=self.image,
        )

        user = User.objects.create(username="testuser")
        user.set_password("12345")
        user.save()
