# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render,render_to_response

# Create your views here.
from django.http import HttpResponse,HttpRequest,HttpResponseRedirect
 
#importing loading from django template 
from django.template import loader,RequestContext
from poll.models import *
from django import *
from rest_framework import viewsets
from .models import *
from .serializers import personSerializer

#our view which is a function named index

def artist_(request):
    
    artist_=artist.objects.all()
    return render_to_response('artists.html',{'artist_': artist_})
    #return render_to_response('artists.html',{'year_formed': year_formed})
    """template = loader.get_template('artists.html')
    return HttpResponse(template.render())"""

def artistdetails(request,id):
    artist_=artist.objects.get(pk=id)
    return render_to_response('artistdetails.html',{'artist':artist_})

def create_form(request):
    if request.method=='GET':
        form=artistform()
        return render(request,'create_form.html',{'form': form})
    elif request.method=='POST':
        form=artistform(request.POST)
        form.save()
        return HttpResponseRedirect('/artists') 



def index(request):
    
    #getting our template 
    template = loader.get_template('index.html')
    

    #rendering the template in HttpResponse
    return HttpResponse(template.render())

def Index(request):
    template1 = loader.get_template('index1.html')

    #rendering the template in HttpResponse
    return HttpResponse(template1.render())      

def Index2(request):
    template2 = loader.get_template('index2.html')

    #rendering the template in HttpResponse
    return HttpResponse(template2.render()) 

def Index3(request):
    template3 = loader.get_template('index_form.html')

    #rendering the template in HttpResponse
    return HttpResponse(template3.render()) 

def persons_details(request):
    template3 = loader.get_template('person_details.html')

    #rendering the template in HttpResponse
    return HttpResponse(template3.render()) 

def personal_details_form_(request):
    #import pdb;pdb.set_trace()
    if request.method=='GET':
        #import pdb;pdb.set_trace()
        form=person_details_form()
        return render(request,'create_form.html',{'form': form}) 
    #import pdb;pdb.set_trace()       
    elif request.method=='POST':  
        #import pdb;pdb.set_trace()    
        form=person_details_form(request.POST)
        form.save()
        return HttpResponseRedirect('/persondetails')

 
class personViewSet(viewsets.ModelViewSet):
    queryset = persondetails.objects.all()
    serializer_class = personSerializer        
    

def brown_bear_pics(request):
    template4 = loader.get_template('brown_bear_pics.html')

    #rendering the template in HttpResponse
    return HttpResponse(template4.render())

def contact(request):
    template5 = loader.get_template('contact.html')

    #rendering the template in HttpResponse
    return HttpResponse(template5.render())

def JS_test(request):
    template6 = loader.get_template('index_js_test.html')

    #rendering the template in HttpResponse
    return HttpResponse(template6.render())    