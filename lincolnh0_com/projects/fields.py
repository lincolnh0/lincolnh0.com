from django.forms.widgets import ClearableFileInput


class BulmaClearableFileInput(ClearableFileInput):
    template_name = "fields/clearable_file_input.html"
