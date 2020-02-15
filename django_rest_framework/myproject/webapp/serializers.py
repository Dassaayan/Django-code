from rest_framework import serializers
#from rest_framework import web_movies
import sys
from .models import Movies
from .models import Episodes


class web_moviesSerializer(serializers.ModelSerializer):

	class Meta:
		model=Movies
		fields='__all__'

class web_episodesSerializer(serializers.ModelSerializer):

	class Meta:
		model=Episodes
		fields='__all__'		

