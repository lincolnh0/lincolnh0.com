from django.views.generic import (
    DetailView,
    ListView,
)
from .models import Project


class ProjectDetailView(DetailView):
    model = Project

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = self.object.title
        return context


projects_detail_view = ProjectDetailView.as_view()


class ProjectListView(ListView):
    model = Project

    def get_queryset(self):
        projects = (
            Project.objects.filter(is_published=True).order_by("created").reverse()
        )
        return projects

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Projects"
        return context


projects_list_view = ProjectListView.as_view()
