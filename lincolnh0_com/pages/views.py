from django.views.generic import TemplateView

from lincolnh0_com.blog.models import Post
from lincolnh0_com.projects.models import Project


class LandingPageView(TemplateView):
    template_name = "pages/home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Home"
        context["featured_projects"] = (
            Project.objects.filter(featured=True).order_by("created").reverse()[:3]
        )

        context["latest_posts"] = (
            Post.objects.filter(is_published=True).order_by("created").reverse()[:5]
        )
        return context


landing_page_view = LandingPageView.as_view()
