# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from django.db import models
from django import forms



class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class Login(models.Model):
    first_name = models.CharField(max_length=300, blank=True, null=True)
    middle_name = models.CharField(max_length=300, blank=True, null=True)
    last_name = models.CharField(max_length=200, blank=True, null=True)
    email_id = models.CharField(max_length=300, blank=True, null=True)
    password = models.CharField(max_length=500, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'login'



class BlogCommentsForm(forms.ModelForm):
    class Meta:
        model= Login
        fields= ["first_name","middle_name", "last_name", "email_id", "password"]


