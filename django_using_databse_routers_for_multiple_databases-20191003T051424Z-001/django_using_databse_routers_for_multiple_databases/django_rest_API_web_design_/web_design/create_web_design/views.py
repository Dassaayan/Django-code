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

def bootstrap_html(request):
    template1 = loader.get_template('bootstrap.html')
    #rendering the template in HttpResponse
    return HttpResponse(template1.render())