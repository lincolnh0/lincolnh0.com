from django.urls import path

from .views import (
    blog_detail_view,
    blog_list_view,
)

app_name = "blog"
urlpatterns = [
    path("", view=blog_list_view, name="list"),
    path("<slug:slug>", view=blog_detail_view, name="detail"),
]
