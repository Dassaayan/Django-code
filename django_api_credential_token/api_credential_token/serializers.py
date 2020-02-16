from api_credential_token.models import EmployeeDetails,Employee,EmployeeSalary
from rest_framework import serializers,fields

class employeeSerializer(serializers.ModelSerializer):
    #import pdb;pdb.set_trace()
    Employee_Name=serializers.CharField(source='employee_name')
    Employee_ID=serializers.CharField(source='employee_id')
    class Meta:
        model =Employee
        fields =['Employee_ID','Employee_Name']


class Employee_SalarySerializer(serializers.ModelSerializer):
    employee=employeeSerializer()
    class Meta:
        model =EmployeeSalary
        fields=['employee','employee_salary_monthly']        


class Employee_DetailsSerializer(serializers.ModelSerializer):
    Employee_Addr=serializers.CharField(source='employee_addr')
    Employee_contact_No=serializers.CharField(source='employee_mobile_number')     
    Post=serializers.CharField(source='employee_designation')   
    City=serializers.CharField(source='employee_city') 
    Blood_Group=serializers.CharField(source='employee_blood_grp') 
    employee=employeeSerializer()
    class Meta:
        model=EmployeeDetails
        fields=['id','employee','Employee_Addr','Employee_contact_No','Post'
                  ,'City','Blood_Group','doj']                 

        
