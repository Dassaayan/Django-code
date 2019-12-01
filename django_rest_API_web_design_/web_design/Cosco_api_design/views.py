# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render,render_to_response

# Create your views here.
from django.http import HttpResponse,HttpRequest,HttpResponseRedirect
 
#importing loading from django template 
from django.template import loader,RequestContext
from django import *
from Cosco_api_design.models import *
from rest_framework import viewsets
from rest_framework.views import APIView
from .models import *
from .serializers import *
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.decorators import list_route
from rest_framework.response import Response
 # <-- Here

# Create your views here.


class coscoapiView(viewsets.ModelViewSet):
    #import pdb;pdb.set_trace()
    queryset = ContainerTrackingKeepup.objects.using('Cosco_Shipment_db').all()
    serializer_class = cosco_details_serializer


