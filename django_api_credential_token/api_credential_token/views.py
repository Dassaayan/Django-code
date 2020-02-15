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
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated 
from rest_framework.decorators import list_route
from rest_framework.response import Response
 # <-- Here

# Create your views here.


class employeeViewSet(viewsets.ModelViewSet):
    # permission_classes = (IsAuthenticated,)
    #import pdb;pdb.set_trace()
    queryset = EmployeeDetails.objects.all()
    serializer_class = Employee_DetailsSerializer

# class employeeFilteredViewSet(viewsets.ModelViewSet):
#     #import pdb;pdb.set_trace()
#     # permission_classes = (IsAuthenticated,)
#     queryset = Employee.objects.all()
#     serializer_class = employee
#     @list_route()
#     def employee_filtered(self, request, id=None):
#         #serializers.serialize('json', self.queryset)
#         #import pdb;pdb.set_trace()
#         serializer_employees = self.get_serializer(self.queryset.filter(employee_id=id), many=True)
#         return Response(serializer_employees.data)