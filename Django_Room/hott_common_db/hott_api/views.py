# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render,get_object_or_404
# Create your views here.
from rest_framework.decorators import action
from rest_framework import viewsets
from rest_framework.response import Response
from .serializers import ApiCommontableSerializer
from .models import ApiCommontable


class ApiCommontableViewSet(viewsets.ModelViewSet):
    queryset = ApiCommontable.objects.all().order_by('title')
    serializer_class = ApiCommontableSerializer

class ApiCommontableViewSet_filter(viewsets.ModelViewSet):
    queryset = ApiCommontable.objects.all()
    serializer_class = ApiCommontableSerializer
    @action(detail=True, methods=['get'])
    def filtered(self,request,source_id=None):
        serializer = self.get_serializer(self.queryset.filter(source_id=source_id), many=True)
        return Response(serializer.data)    