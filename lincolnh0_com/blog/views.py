from django.views.generic import (
    DetailView,
    ListView,
)
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
        projects = (
            Post.objects.filter(is_published=True).order_by("created").reverse()
        )
        return projects

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Blog posts"
        context["tag_line"] = "Intermittent and unsolicited updates on anything and everything."
        return context


blog_list_view = BlogListView.as_view()
