# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Movies
from .serializers import web_moviesSerializer
from .models import Episodes
from .serializers import web_episodesSerializer

class movieList(APIView):
    def get(self,request):
        
        queryset1 = Movies.objects.all()
        serializer_class1 = web_moviesSerializer(queryset1,many=True)
        return Response(serializer_class1.data)

class episodeList(APIView):
    def get(self,request):
        
        queryset2 = Episodes.objects.all()
        serializer_class2 = web_episodesSerializer(queryset2,many=True)
        return Response(serializer_class2.data)         

	def post(self,):
	    pass	