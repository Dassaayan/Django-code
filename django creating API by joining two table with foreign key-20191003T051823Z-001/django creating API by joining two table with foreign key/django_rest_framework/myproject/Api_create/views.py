# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render,render_to_response

# Create your views here.
from django.http import HttpResponse,HttpRequest,HttpResponseRedirect
 
#importing loading from django template 
from django.template import loader,RequestContext
from django import *
from Api_create.models import *
from rest_framework import viewsets
from .models import *
from .serializers import MovieSerializer,ModelSerializer_credits
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated 
from rest_framework.decorators import list_route
from rest_framework.response import Response
 # <-- Here

# Create your views here.


class movieViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    #import pdb;pdb.set_trace()
    queryset = NetflixMovies.objects.all()
    serializer_class = MovieSerializer(many =True)

class MovieFilteredViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    queryset = NetflixMovies.objects.all()
    serializer_class = MovieSerializer
    @list_route()
    def movie_filtered(self, request,id=None):
        serializer_movies = self.get_serializer(self.queryset.filter(id=id), many=True)
        return Response(serializer_movies.data)
        
"""class MovieFilteredViewSet_credits(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    queryset_credits=NetflixMoviesCredits.objects.all()
    serializer_class = ModelSerializer_credits
    @list_route()
    def movie_filtered_credits(self, request, id=None):
        serializer_credits=self.get_serializer(self.queryset_credits.filter(movie_id=id), many=True)
        return Response(serializer_credits.data)"""

