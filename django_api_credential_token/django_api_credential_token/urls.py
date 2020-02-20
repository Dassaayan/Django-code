"""django_api_credential_token URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url,include
from django.contrib import admin
from rest_framework.urlpatterns import format_suffix_patterns
from django.contrib import admin
from rest_framework import routers
from api_credential_token import views
from django.urls import *
from django.views.generic import TemplateView 
from django.conf import settings


urlpatterns = [

    url(r'^employeeviewSets/api/details=(?P<string>\w+)',views.employeeViewSet.as_view({'get':'get_set'}),name='get_set') ,
    url(r'^employeeviewSets/api/employee/id=(?P<id>\d+)', 
        views.employeeFilteredViewSet.as_view({'get': 'employee_filtered'}), name='employee_filtered'),
    url(r'^employeeview/api/employee/salary/emp_id=(?P<id>\d+)', 
        views.employeeFilteredSalaryViewSet.as_view({'get': 'employee_salary_filtered'}), name='employee_salary_filtered'),
    url('employeeviewSets/api/login', views.login),
 ]     


