from django.urls import path
from . import views

urlpatterns = [
    path("path2/", views.func2),
]