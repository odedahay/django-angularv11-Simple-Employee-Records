from django.db import models

class Deparments(models.Model):
    DepartmentId = models.AutoField(primary_key=True)
    DepartmentName = models.CharField(max_length=100)

class Employees(models.Model):
    EmployeeId = models.AutoField(primary_key=True)
    EmployeeName = models.CharField(max_length=200)
    Department = models.CharField(max_length=200)
    DateOfJoining = models.DateField()
    PhotoFileName = models.CharField(max_length=100)