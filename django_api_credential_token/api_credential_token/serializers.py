from api_credential_token.models import EmployeeDetails,Employee,EmployeeSalary
from rest_framework import serializers,fields

class employeeSerializer(serializers.ModelSerializer):
    #import pdb;pdb.set_trace()
    class Meta:
        model =Employee
        fields =['employee_id','employee_name']


class Employee_SalarySerializer(serializers.ModelSerializer):
    class Meta:
        model =EmployeeSalary
        fields=['employee_salary_monthly']        


class Employee_DetailsSerializer(serializers.ModelSerializer):
    employee=employeeSerializer()
    # emp_sal=Employee_SalarySerializer()
    class Meta:
        model=EmployeeDetails
        fields=['id','employee','employee_addr','employee_mobile_number','employee_designation','employee_city','employee_blood_grp',
               'doj']
        depth=1 