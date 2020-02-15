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
#from poll.file_upload_validation import ContentTypeRestrictedFileField
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token

@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)

class NetflixMovies(models.Model):
    id = models.AutoField(primary_key=True)
    movie_name = models.CharField(db_column='Movie_name', max_length=500)  # Field name made lowercase.
    airdate = models.CharField(db_column='Airdate', max_length=10, blank=True, null=True)  # Field name made lowercase.
    rating = models.CharField(db_column='Rating', max_length=10, blank=True, null=True)  # Field name made lowercase.
    duration = models.CharField(db_column='Duration', max_length=10, blank=True, null=True)  # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=3000, blank=True, null=True)  # Field name made lowercase.
    production_country = models.CharField(db_column='Production_country', max_length=1000, blank=True, null=True)  # Field name made lowercase.
    added_to_netflix = models.CharField(db_column='Added_to_netflix', max_length=100, blank=True, null=True)  # Field name made lowercase.
    category = models.CharField(db_column='Category', max_length=100, blank=True, null=True)  # Field name made lowercase.
    movie_url = models.CharField(db_column='Movie_url', max_length=1000, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'netflix_movies'
        
        
class NetflixMoviesCredits(models.Model):
    movie= models.ForeignKey(NetflixMovies,on_delete=models.CASCADE, related_name='movie_credits',null=False, blank=False)  # Field name made lowercase.
    credit_type = models.CharField( max_length=100, blank=True, null=True)  # Field name made lowercase.
    credit_name = models.CharField( max_length=500, blank=True, null=True)  # Field name made lowercase.    

    class Meta:
        managed = False
        db_table = 'Api_create_netflixmoviescredits'   
        