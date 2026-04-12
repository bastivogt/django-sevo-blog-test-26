from django.urls import path

from sevo_blog import views

app_name = "sevo_blog"
urlpatterns = [
    path("", views.index, name="index"),
]