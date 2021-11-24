from django.urls import path

from .views import blog_create_view, blog_detail_view, blog_list_view, blog_update_view

app_name = "blog"
urlpatterns = [
    path("", view=blog_list_view, name="list"),
    path("add", view=blog_create_view, name="create"),
    path("<int:pk>/update", view=blog_update_view, name="update"),
    path("<slug:slug>", view=blog_detail_view, name="detail"),
]
