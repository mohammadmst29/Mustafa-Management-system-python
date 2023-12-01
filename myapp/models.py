from django.db import models

# Create your models here.
class Student_Model(models.Model):

    First_Name=models.CharField(max_length=100,null=True)
    Last_Name=models.CharField(max_length=100)
    DepartMent_Name=models.CharField(max_length=100)
    Mobile_Number=models.CharField(max_length=100)
 

    def __str__(self):
        return self.FirstName+" "+self.LastName
    
class Teacher_Model(models.Model):

    First_Name=models.CharField(max_length=100,null=True)
    Last_Name=models.CharField(max_length=100)
    DepartMent_Name=models.CharField(max_length=100)
    Mobile_Number=models.CharField(max_length=100)


    def __str__(self):
        return self.FirstName+" "+self.LastName
    
class Employee_Model(models.Model):

    First_Name=models.CharField(max_length=100,null=True)
    Last_Name=models.CharField(max_length=100)
    DepartMent_Name=models.CharField(max_length=100)
    Mobile_Number=models.CharField(max_length=100)


    def __str__(self):
        return self.FirstName+" "+self.LastName