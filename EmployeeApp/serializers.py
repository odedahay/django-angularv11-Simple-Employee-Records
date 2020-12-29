from rest_framework import serializers
from EmployeeApp.models import Deparments, Employees


class DepartmentSerializer(serializers.ModelSerializer):
     class Meta:
         model = Deparments
         fields = ('DepartmentId', 'DepartmentName')

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employees
        fields = ('EmployeeId',
                  'EmployeeName',
                  'Department',
                  'DateOfJoining',
                  'PhotoFileName')