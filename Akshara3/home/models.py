from django.db import models

# Create your models here.
# very important -> table name => home_employeemodel
class EmployeeModel(models.Model):
    eid = models.IntegerField()
    ename = models.CharField(max_length=30)
    emp = models.CharField(max_length=30)
    esalary = models.IntegerField()

    def __str__(self):
        return self.ename