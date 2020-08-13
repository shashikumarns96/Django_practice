from django.urls import path

from home.views import *

urlpatterns = [
    path('enter_emp/', enter_emp),
    path('enter_emp_post/', enter_emp_post),
    path('enter_employee/', enter_employee),
    path('show/', show),
    path('delete/<int:eno>/', delete),
    path('update/<int:eno>/', update),
    path('update1/<int:eno>/',update_u),
    path('delete1/<str:ename>/',delete_d),
]