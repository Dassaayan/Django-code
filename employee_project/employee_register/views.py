# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render,redirect
from .forms import *
from .models import *

# Create your views here.

def employee_list(request):
    context= {'employee_list':Employee.objects.all()}
    return render(request,"employee_register/employee_list.html",context)

def employee_form(request):
    if request.method=="GET":
        form =EmployeeForm()
        return render(request,"employee_register/employee_form.html",{"form":form})
    else:
        form =EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/employee/list/')         

def employee_delete(request):
    pass