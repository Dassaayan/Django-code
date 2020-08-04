# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import *

# Register your models here.
@admin.register(HbogoPrograms)
class HbogoPrograms_admin(admin.ModelAdmin):
    list_display='__all__'#('launch_id', 'show_type', 'title', 'series_title')
    ordering = ('launch_id',)
    search_fields = ('title',)
    list_filter = ('show_type', )

@admin.register(ShowtimePrograms)
class ShowtimePrograms_admin(admin.ModelAdmin):
    list_display=('source_program_id', 'item_type', 'title',)
    ordering = ('source_program_id',)
    search_fields = ('title',)
    list_filter = ('item_type', )

@admin.register(StarzPrograms)
class StarzPrograms_admin(admin.ModelAdmin):
    list_display=('program_id', 'item_type', 'title', 'episode_title')
    ordering = ('program_id',)
    search_fields = ('title',)
    list_filter = ('item_type', )