from django.urls import path
from django.views.generic.base import RedirectView

from . import views

app_name = "books"

urlpatterns = [
    path("app/", views.IndexView.as_view(), name="index"),
    path("", RedirectView.as_view(url="app")),
]
