from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView, DetailView, ListView, UpdateView

from .forms import ProjectForm
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
    paginate_by = 12

    def get_queryset(self):
        projects = (
            Project.objects.filter(is_published=True).order_by("created").reverse()
        )
        return projects

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Projects"
        context["tag_line"] = "From sandbox ideas to fully built projects."
        return context


projects_list_view = ProjectListView.as_view()


class ProjectCreateView(LoginRequiredMixin, CreateView):
    """
    Create view for new project page.
    """

    model = Project
    form_class = ProjectForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Create a project"
        return context


project_create_view = ProjectCreateView.as_view()


class ProjectUpdateView(LoginRequiredMixin, UpdateView):
    """
    Update view for existing project page.
    """

    model = Project
    form_class = ProjectForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Editing " + context["object"].title
        return context


project_update_view = ProjectUpdateView.as_view()
