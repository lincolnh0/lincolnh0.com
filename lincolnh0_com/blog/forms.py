from ckeditor_uploader.widgets import CKEditorUploadingWidget
from django import forms

from .models import Post


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = (
            "title",
            "body",
            "is_published",
        )
        widgets = {
            "title": forms.TextInput(attrs={"class": "input"}),
            "body": CKEditorUploadingWidget(attrs={"class": "textarea"}),
            "is_published": forms.CheckboxInput(attrs={"class": "checkbox"}),
        }
