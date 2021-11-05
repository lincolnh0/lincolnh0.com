from django.urls import path

from .views import (
    projects_detail_view,
    projects_list_view,
)

app_name = "projects"
urlpatterns = [
    path("", view=projects_list_view, name="list"),
    path("<slug:slug>", view=projects_detail_view, name="detail"),
]
