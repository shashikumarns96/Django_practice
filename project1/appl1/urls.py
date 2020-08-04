from django.urls import path
from . import views

urlpatterns = [
    path("path1/", views.func1),
]