from .models import *
from rest_framework import serializers,fields
from .models import *


class cosco_details_serializer(serializers.ModelSerializer):        
    class Meta:
        model =ContainerTrackingKeepup
        fields='__all__'

 
    




 
