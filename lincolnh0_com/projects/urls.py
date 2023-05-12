from django.urls import path

from .views import (
    project_create_view,
    project_update_view,
    projects_detail_view,
    projects_list_view,
)

app_name = "projects"
urlpatterns = [
    path("", view=projects_list_view, name="list"),
    path("add", view=project_create_view, name="create"),
    path("<int:pk>/update", view=project_update_view, name="update"),
    path("<slug:slug>", view=projects_detail_view, name="detail"),
]
