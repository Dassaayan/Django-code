# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import connections
from django.db import models
# Create your models here.


class Movies(models.Model):
    movie_name=models.CharField(primary_key=True, max_length=254)
    movies_id=models.IntegerField(unique=True)
    movie_description=models.CharField(max_length=1000,blank=True,null=True)
    movie_duration=models.CharField(max_length=100,blank=True,null=True) 
    movie_rating=models.CharField(max_length=100,blank=True,null=True)
    realease_year=models.IntegerField(blank=True,null=True)            
    class Meta:
        managed = False
        db_table='Movies'

    def __str__(self):
        return self.movie_name
        return self.movies_id   
        return self.movie_description
        return self.movie_duration
        return self.movie_rating
        return self.realease_year


class Episodes(models.Model):
    episode_id = models.AutoField(db_column='Episode_Id', primary_key=True)  # Field name made lowercase.
    title = models.CharField(max_length=1000, blank=True, null=True)
    episode_title = models.CharField(max_length=1000, blank=True, null=True)
    show_id = models.IntegerField(blank=True, null=True)
    content_id = models.CharField(unique=True, max_length=254, blank=True, null=True)
    airdate = models.CharField(max_length=500, blank=True, null=True)
    season_number = models.CharField(max_length=10, blank=True, null=True)
    episode_number = models.CharField(max_length=10, blank=True, null=True)
    duration = models.CharField(max_length=50, blank=True, null=True)
    description = models.CharField(max_length=5000, blank=True, null=True)
    image_url = models.CharField(max_length=4000, blank=True, null=True)
    url = models.CharField(max_length=4000, blank=True, null=True)
    status_field = models.CharField(db_column='status_', max_length=100, blank=True, null=True)  # Field renamed because it ended with '_'.
    expiry_date = models.CharField(max_length=500, blank=True, null=True)
    is_paid_content = models.CharField(max_length=100, blank=True, null=True)
    isusersubscriber = models.CharField(db_column='isUserSubscriber', max_length=100, blank=True, null=True)  # Field name made lowercase.
    alternate_title = models.CharField(max_length=500, blank=True, null=True)
    datatracking = models.CharField(db_column='dataTracking', max_length=2000, blank=True, null=True)  # Field name made lowercase.
    episodes_url = models.CharField(max_length=1000, blank=True, null=True)
    rating = models.CharField(max_length=500, blank=True, null=True)
    is_live = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Episodes'

    def __str__(self):
    	return [self.episode_id,
         [{"title":self.title,"alternate_title":self.alternate_title}],
    	 self.episode_title,self.show_id,self.content_id,self.airdate,[{"Season_number":self.season_number,"episode_number":self.episode_number}],
    	self.duration, self.description,
        [{"image_url":self.image_url,"url":self.url,"episodes_url":self.episodes_url}] ,
        [{"status_field":self.status_field,"expiry_date":self.expiry_date,"is_paid_content":self.is_paid_content,"isusersubscriber":self.isusersubscriber}],
        self.datatracking,[{"rating":self.rating,"is_live":self.is_live}]]


class Series(models.Model):
    show_id = models.AutoField(primary_key=True)
    show_name = models.CharField(primary_key=True, max_length=254)
    show_description = models.CharField(max_length=2000, blank=True, null=True)
    availability = models.CharField(max_length=500, blank=True, null=True)
    show_url = models.CharField(max_length=500, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Series'