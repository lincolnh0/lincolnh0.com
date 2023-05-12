from ckeditor_uploader.widgets import CKEditorUploadingWidget
from django import forms

from .fields import BulmaClearableFileInput
from .models import Project


class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = (
            "title",
            "tag_line",
            "body",
            "header_image",
            "source_link",
            "demo_link",
            "featured",
            "is_published",
        )
        widgets = {
            "title": forms.TextInput(attrs={"class": "input"}),
            "tag_line": forms.TextInput(attrs={"class": "input"}),
            "body": CKEditorUploadingWidget(attrs={"class": "textarea"}),
            "header_image": BulmaClearableFileInput(attrs={"class": "file-input"}),
            "source_link": forms.TextInput(attrs={"class": "input"}),
            "demo_link": forms.TextInput(attrs={"class": "input"}),
            "featured": forms.CheckboxInput(attrs={"class": "checkbox"}),
            "is_published": forms.CheckboxInput(attrs={"class": "checkbox"}),
        }
