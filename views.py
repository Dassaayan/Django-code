from __future__ import unicode_literals
from django.shortcuts import render,render_to_response
# Create your views here.
from django.http import HttpResponse,HttpRequest,HttpResponseRedirect
from django.template import loader,RequestContext
from rest_framework import viewsets
from django.core import serializers
from .serializers import *
import json
from collections import OrderedDict
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated,AllowAny 
from rest_framework.decorators import list_route,api_view, permission_classes,action
 # <-- Here
from django.contrib.auth import authenticate
from django.views.decorators.csrf import csrf_exempt 
from rest_framework.status import (
    HTTP_400_BAD_REQUEST,
    HTTP_404_NOT_FOUND,
    HTTP_200_OK
)
#Now we write login function which returns the token associated with the user and make api route for the same using.
@csrf_exempt
@api_view(["POST"])
@permission_classes((AllowAny,))
def login(request):
    username = request.data.get("username")
    password = request.data.get("password")
    if username is None or password is None:
        return Response({'error': 'Please provide both username and password'},
                        status=HTTP_400_BAD_REQUEST)
    user = authenticate(username=username, password=password)
    if not user:
        return Response({'error': 'Invalid Credentials'},
                        status=HTTP_404_NOT_FOUND)
    token, _ = Token.objects.get_or_create(user=user)
    return Response({'token': token.key},
                    status=HTTP_200_OK)

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
    #permission_classes = (IsAuthenticated,)
    #import pdb;pdb.set_trace()
    queryset = EmployeeDetails.objects.all()
    serializer_class = Employee_DetailsSerializer  
    @list_route()
    def get_set(self,request,string=None):
        #import pdb;pdb.set_trace()
        if string=="true":
            serializer_employees = self.get_serializer(self.queryset, many=True)
        if self.request.GET.get('Authorization')=="Token Xapi_key":
            return Response(serializer_employees.data,
                        status=HTTP_200_OK)
        else:
            return Response({'error': 'Invalid Token'},
                            status=HTTP_404_NOT_FOUND)
      
            
class employeeFilteredViewSet(viewsets.ModelViewSet):
    #import pdb;pdb.set_trace()
    # permission_classes = (IsAuthedumpsnticated,)
    queryset = EmployeeDetails.objects.all()
    serializer_class = Employee_DetailsSerializer
    @list_route()
    def employee_filtered(self, request, id=None):
        #serializers.serialize('json', self.queryset)
        username = request.data.get("username")
        password = request.data.get("password")
        if username is None or password is None:
            return Response({'error': 'Please provide both username and password'},
                            status=HTTP_400_BAD_REQUEST)
        user = authenticate(username=username, password=password)
        if not user:
            return Response({'error': 'Invalid Credentials'},
                            status=HTTP_404_NOT_FOUND)
        serializer_employees = self.get_serializer(self.queryset.filter(employee_id=id), many=True)    
        token, _ = Token.objects.get_or_create(user=user)
        return Response(modify_data_api().modify_API(json.dumps(serializer_employees.data)),
                        status=HTTP_200_OK)

class employeeFilteredSalaryViewSet(viewsets.ModelViewSet):
    #import pdb;pdb.set_trace()
    # permission_classes = (IsAuthenticated,)
    queryset = EmployeeSalary.objects.all()
    serializer_class = Employee_SalarySerializer
    @list_route()
    def employee_salary_filtered(self, request, id=None):
        #serializers.serialize('json', self.queryset)
        #import pdb;pdb.set_trace()
        if request.GET.get('Authorization')=="Token Xapi_key":
            serializer_employees = self.get_serializer(self.queryset.filter(employee=id), many=True)
            return Response(modify_data_api().modify_API_salary(json.dumps(serializer_employees.data)))
        else:
            return Response({'error': 'Invalid Token'},
                            status=HTTP_404_NOT_FOUND)        