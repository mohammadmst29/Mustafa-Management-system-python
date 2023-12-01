from django.contrib import admin
from myapp.models import Student_Model,Teacher_Model,Employee_Model

# Register your models here.
admin.site.register(Student_Model)
admin.site.register(Teacher_Model)
admin.site.register(Employee_Model)