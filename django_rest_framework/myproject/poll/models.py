# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django import forms

# Create your models here.
class artist(models.Model):
    name=models.CharField("artist",max_length=50)
    year_formed=models.IntegerField()

class artistform(forms.ModelForm):
    class Meta:
        model=artist
        fields=['name','year_formed']    


class album(models.Model):
    name=models.CharField("album",max_length=50)
    artist=models.ForeignKey(artist) 

class persondetails(models.Model):
    firstname=models.CharField(unique=True,max_length=30)
    lastname=models.CharField(max_length=20)
    
    def __unicode__(self):
        return self.firstname
        return self.lastname

class person_details_form(forms.ModelForm):
    class Meta:
        model=persondetails
        fields='__all__'
        

