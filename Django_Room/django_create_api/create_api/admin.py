#*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from django_restful_admin import admin as api_admin
from .models import *
# Register your models here.

@admin.register(ShowtimePrograms)
class ShowtimePrograms_admin(admin.ModelAdmin):
    list_display=('source_program_id','series_id', 'item_type', 'title','description','img_url','url','season_number','episode_number','created_at','updated_at','expired')
    ordering = ('season_number',)
    search_fields = ('title',)
    list_filter = ('item_type','expired')

# @api_admin.register(ShowtimePrograms)  
# class MyCustomApiAdmin(BaseRestFulModelAdmin):

# 	@api_admin.action(permission='ShowtimePrograms.view_product', detail=True, methods=['GET'], url_path=r'ShowtimePrograms/source_id/(?P<source_program_id>\d+)')  
# 	def my_custom_action(self, request, pk, source_program_id):