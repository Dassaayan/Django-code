# serializers.py
from rest_framework import serializers

from .models import ShowtimePrograms

class ShowtimeProgramsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ShowtimePrograms
        fields ='__all__' 
