from .models import *
from rest_framework import serializers,fields
from .models import NetflixMovies,NetflixMoviesCredits


class ModelSerializer_credits(serializers.ModelSerializer):        
    #movie_set=MovieSerializer(many=True,read_only=True)
    class Meta:
        model =NetflixMoviesCredits
        fields=['id','credit_type','credit_name']

 
class MovieSerializer(serializers.ModelSerializer):
    movie_credits =ModelSerializer_credits(read_only=True,many=True)

    class Meta:
        model =NetflixMovies
        fields = ('id','movie_name','description','duration','rating','airdate'
                      ,'category','movie_url','movie_credits','production_country','added_to_netflix')
    




 
