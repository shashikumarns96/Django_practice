from django.urls import path
from . import views

urlpatterns = [
    path('',views.func2),
    path('emp_get/',views.employee),
    path('emp_post/', views.employee_post),
]