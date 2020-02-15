"""web_design URL Configuration

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
from django.conf.urls import url
from django.contrib import admin

from django.conf.urls import url,include
from django.contrib import admin
from rest_framework .urlpatterns import format_suffix_patterns
from django.contrib import admin
from rest_framework import routers
from Cosco_api_design import views
from create_web_design import views
from django.contrib import admin
from django.urls import *
from django.views.generic import TemplateView 
from django.conf import settings
from django.conf.urls import url, include


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^register/users',views.Index_html,name='Index_html'),
    url(r'^bootstrap/page/learning',views.bootstrap_html,name='bootstrap_html'),
    url(r'^Cosco/api',include('Cosco_api_design.urls'))
]
