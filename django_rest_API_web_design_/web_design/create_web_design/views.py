# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse,HttpRequest,HttpResponseRedirect 
#importing loading from django template 
from django.template import loader,RequestContext
from django import *
from rest_framework import viewsets
from .models import *


def Index_html(request):
    template1 = loader.get_template('web_portal_registration.html')
    #rendering the template in HttpResponse
    return HttpResponse(template1.render())

def Index_html_demo(request):
    template2 = loader.get_template('html_file.html')
    #rendering the template in HttpResponse
    return HttpResponse(template2.render())    

def bootstrap_html(request):
    template1 = loader.get_template('bootstrap.html')
    #rendering the template in HttpResponse
    return HttpResponse(template1.render())

def login_details(request):
    if request.method == 'POST':
        #import pdb;pdb.set_trace()
        if request.POST.get('firstname') and request.POST.get('middlename') and request.POST.get('lastname') and request.POST.get('email') and request.POST.get('password'):
            #import pdb;pdb.set_trace()
            post=BlogCommentsForm()
            post.first_name= request.POST.get('firstname')
            post.middle_name= request.POST.get('middlename')
            post.last_name= request.POST.get('lastname')
            post.email_id= request.POST.get('email')
            post.password= request.POST.get('password')
            post.save()
            
            return HttpResponse(loader.get_template('web_portal_registration.html'))  

    else:
        return HttpResponse(loader.get_template('web_portal_registration.html'))    