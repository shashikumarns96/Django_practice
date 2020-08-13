from django.db import models

# Create your models here.
class EmployeeModel(models.Model):
    emp_id = models.IntegerField()
    emp_name = models.CharField(max_length=30)

class SchoolModel(models.Model):
    name = models.CharField(max_length=25)
    id = models.IntegerField()