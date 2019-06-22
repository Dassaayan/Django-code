from rest_framework import serializers
from .models import persondetails
 
class personSerializer(serializers.ModelSerializer):
    class Meta:
        model =persondetails 
        fields = '__all__'
 
