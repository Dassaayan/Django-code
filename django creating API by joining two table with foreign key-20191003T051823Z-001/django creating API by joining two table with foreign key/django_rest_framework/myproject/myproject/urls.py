"""myproject URL Configuration

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
from rest_framework .urlpatterns import format_suffix_patterns
#from webapp import views
from django.contrib import admin
from rest_framework import routers
#from poll import views
from Api_create import views
from django.contrib import admin
from django.urls import *
from django.views.generic import TemplateView 
from django.conf import settings
from django.conf.urls import url, include


urlpatterns = [

    url(r'^movieviewSets/api',include('Api_create.urls')) ,
    url(r'^movieviewSets/api/Movies/id/(?P<id>\d+)', views.MovieFilteredViewSet.as_view({'get': 'movie_filtered'}), name='movie_filtered'),
    #url(r'^movie/id/(?P<id>\d+)$', views.MovieFilteredViewSet_credits.as_view({'get': 'movie_filtered_credits'}), name='movie_filtered_credits')
 ]     

   
#(?P<id>\d+)Token cc82567f00d6bf451d34fcaee9d7efb8ee4d58ee