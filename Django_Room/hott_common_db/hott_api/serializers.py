# serializers.py
from rest_framework import serializers

from .models import ApiCommontable

class ApiCommontableSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ApiCommontable
        fields ='__all__' 
