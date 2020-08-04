from django.contrib import admin
from .models import *
# Register your models here.

#admin.site.register(ApiCommontable)

# Register your models here.
@admin.register(ApiCommontable)
class ApiCommontable_admin(admin.ModelAdmin):
    list_display=('source_id', 'item_type', 'title', 'episode_title')
    ordering = ('title',)
    search_fields = ('title',)
    list_filter = ('item_type',)
