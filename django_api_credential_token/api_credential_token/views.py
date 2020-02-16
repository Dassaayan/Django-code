from __future__ import unicode_literals

from django.shortcuts import render,render_to_response

# Create your views here.
from django.http import HttpResponse,HttpRequest,HttpResponseRedirect
#importing loading from django template 
from django.template import loader,RequestContext
from django import *
from rest_framework import viewsets
from .models import *
from django.core import serializers
from .serializers import *
import json
from collections import OrderedDict
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated 
from rest_framework.decorators import list_route
from rest_framework.response import Response
 # <-- Here

# Create your views here.
class modify_data_api:

    key_order= ['ID','Employee_ID','Employee_Name','Employee_Addr','Blood_Group','Employee_contact_No','City','DOJ','Post']
    def modify_API(self,dictserializer):
        data_dict=dict()
        for data in eval(dictserializer):
            for keys in data.keys():
                if keys.encode('utf-8')== keys.encode('utf-8')=='doj':
                    key='DOJ'
                    data_dict.update({key:data[keys]}) 
                elif keys.encode('utf-8')=='employee':
                    data_dict.update(data[keys])   
                else:
                    data_dict.update({keys:data[keys]})
        #import pdb;pdb.set_trace()             
        Ordereddict=OrderedDict((k, data_dict[k]) for k in self.key_order)
        print json.dumps([Ordereddict])              
        return [Ordereddict]

    key_order_salary=["Employee_ID","Employee_Name","employee_salary_monthly"]
    def modify_API_salary(self,salary_dictserializer):
        #import pdb;pdb.set_trace()
        data_dict=dict()
        for data in eval(salary_dictserializer):
            for keys in data.keys():
                if keys.encode('utf-8')=='employee':
                    data_dict.update(data[keys])   
                else:
                    data_dict.update({keys:data[keys]})
        #import pdb;pdb.set_trace()             
        Ordereddict=OrderedDict((k, data_dict[k]) for k in self.key_order_salary)
        print json.dumps([Ordereddict])              
        return [Ordereddict]            

class employeeViewSet(viewsets.ModelViewSet):
    # permission_classes = (IsAuthenticated,)
    # import pdb;pdb.set_trace()
    queryset = EmployeeDetails.objects.all()
    serializer_class = Employee_DetailsSerializer

class employeeFilteredViewSet(viewsets.ModelViewSet):
    #import pdb;pdb.set_trace()
    # permission_classes = (IsAuthedumpsnticated,)
    queryset = EmployeeDetails.objects.all()
    serializer_class = Employee_DetailsSerializer
    @list_route()
    def employee_filtered(self, request, id=None):
        #serializers.serialize('json', self.queryset)
        serializer_employees = self.get_serializer(self.queryset.filter(employee_id=id), many=True)
        return Response(modify_data_api().modify_API(json.dumps(serializer_employees.data)))

class employeeFilteredSalaryViewSet(viewsets.ModelViewSet):
    #import pdb;pdb.set_trace()
    # permission_classes = (IsAuthenticated,)
    queryset = EmployeeSalary.objects.all()
    serializer_class = Employee_SalarySerializer
    @list_route()
    def employee_salary_filtered(self, request, id=None):
        #serializers.serialize('json', self.queryset)
        #import pdb;pdb.set_trace()
        serializer_employees = self.get_serializer(self.queryset.filter(employee=id), many=True)
        return Response(modify_data_api().modify_API_salary(json.dumps(serializer_employees.data)))        