# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from django.shortcuts import get_object_or_404
# Create your views here.
from rest_framework.decorators import action
from rest_framework import viewsets
from rest_framework.response import Response
from .serializers import ShowtimeProgramsSerializer
from .models import ShowtimePrograms


class ShowtimeProgramsViewSet(viewsets.ModelViewSet):
    queryset = ShowtimePrograms.objects.all().order_by('title')
    serializer_class = ShowtimeProgramsSerializer

class ShowtimeProgramsViewSet_filter(viewsets.ModelViewSet):
    queryset = ShowtimePrograms.objects.all()
    serializer_class = ShowtimeProgramsSerializer
    @action(detail=True, methods=['get'])
    def filtered(self,request,source_program_id=None):
        serializer = self.get_serializer(self.queryset.filter(source_program_id=source_program_id), many=True)
        return Response(serializer.data)   
