import os
os.environ["DJANGO_SETTINGS_MODULE"] = "Akshara3.settings"
import django
django.setup()

from home.models import EmployeeModel

from faker import Faker

f1 = Faker()
for i in range(50, 100):
    name = f1.name()
    company = f1.company()
    salary = f1.random_number(5, fix_len=True)
    print(i, ":", name, ":", company, ":", salary)
    EmployeeModel.objects.create(eid=i, ename=name, emp=company, esalary=salary)