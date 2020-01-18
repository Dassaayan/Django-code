# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render,redirect
#from .forms import *
from .models import *


def view_web_portal(request):
	return render(request,"web_design/base.html")