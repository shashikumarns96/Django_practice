from django.contrib import admin
from home.models import *


class EmployeeAdmin(admin.ModelAdmin):
    list_display = ['eid', 'ename', 'esalary', 'emp']

# Register your models here.
admin.site.register(EmployeeModel, EmployeeAdmin)

# admin.site.register(EmployeeModel, EmployeeAdmin, modelA, modelAdmin)
# admin.site.register(modelA, modelAdmin)
# admin.site.register(modelB, modelBAdmin)
# admin.site.register(modelC)