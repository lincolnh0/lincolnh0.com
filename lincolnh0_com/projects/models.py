from django.db import models
from django.shortcuts import reverse
from django.utils import timezone
from django.utils import text
from ckeditor.fields import RichTextField


# Create your models here.
class Project(models.Model):
    title = models.CharField(max_length=255)
    tag_line = models.CharField(max_length=200, default="")
    body = RichTextField()

    header_image = models.ImageField(upload_to="projects")

    source_link = models.CharField(max_length=255, default="", blank=True)
    demo_link = models.CharField(max_length=255, default="", blank=True)

    is_published = models.BooleanField()
    featured = models.BooleanField(default=False)
    created = models.DateTimeField(blank=True, null=True)
    changed = models.DateTimeField(blank=True, null=True)
    slug = models.SlugField(default="", max_length=255, blank=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        kwargs = {"slug": self.slug}
        return reverse("projects:detail", kwargs=kwargs)

    def save(self, *args, **kwargs):
        self.slug = text.slugify(self.title, allow_unicode=True)
        self.changed = timezone.now()

        if self.created is None:
            self.created = timezone.now()

        super().save(*args, **kwargs)
