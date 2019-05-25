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

class person_details(models.Model):
	ids=models.IntegerField(primary_key=True)
	Name=models.CharField(max_length=20)
	Email_id=models.CharField(max_length=20)
	Mob_No=models.IntegerField()
	Message=models.CharField(max_length=200)



class person_details_form(forms.ModelForm):
    class Meta:
        model=person_details
        fields=['ids','Name','Email_id','Mob_No','Message']

