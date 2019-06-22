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
from poll import views
from django.contrib import admin
from django.urls import *
 
from django.conf import settings
from django.conf.urls import url, include


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    #url(r'^Movies/', views.movieList.as_view()),
    #url(r'^Episodes/details=json', views.episodeList.as_view()),
    url(r'^Brown_bears/brown_bear_pic', views.brown_bear_pics),
    url(r'^Brown_bears/', views.index),
    url(r'^contact.html', views.contact),
    url(r'^firsttemplate/index1.html', views.Index),
    url(r'^index1.html', views.Index),
    url(r'^index2.html/table', views.Index2),
    url(r'^index_form/form',views.Index3),
    url(r'^artists/',views.artist_, name='artist_'),
    url(r'^artistsdetails/(?P<id>\d+)$',views.artistdetails,name='artistdetails'),
    url(r'^artist/create$',views.create_form,name='create_form'),
    url(r'^detail/create$',views.personal_details_form_,name='personal_details_form_'),
    url(r'^persondetails$',views.persons_details,name='persons_details'),
    url(r'^javascript/test/page$',views.JS_test),
    url(r'^personviewSets/api/', include('poll.urls')),

]
