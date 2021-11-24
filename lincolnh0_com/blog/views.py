from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView, DetailView, ListView, UpdateView

from .forms import PostForm
from .models import Post


class BlogDetailView(DetailView):
    model = Post

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = self.object.title
        return context


blog_detail_view = BlogDetailView.as_view()


class BlogListView(ListView):
    model = Post
    paginate_by = 12

    def get_queryset(self):
        projects = Post.objects.filter(is_published=True)
        year = self.request.GET.get("year")
        if year:
            projects = projects.filter(created__year=year)
        projects = projects.order_by("created").reverse()

        return projects

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Blog posts"
        year = self.request.GET.get("year")
        if year:
            context["title"] += " in " + str(year)
        context["tag_line"] = "Intermittent updates on anything and everything."

        context["years"] = Post.objects.dates("created", "year", order="DESC")
        return context


blog_list_view = BlogListView.as_view()


class BlogCreateView(LoginRequiredMixin, CreateView):
    """
    Create view for new blog page.
    """

    model = Post
    form_class = PostForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Create a post"
        return context


blog_create_view = BlogCreateView.as_view()


class BlogUpdateView(LoginRequiredMixin, UpdateView):
    """
    Update view for existing blog page.
    """

    model = Post
    form_class = PostForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Editing " + context["object"].title
        return context


blog_update_view = BlogUpdateView.as_view()
