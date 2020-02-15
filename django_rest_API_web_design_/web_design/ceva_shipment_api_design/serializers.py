from .models import *
from rest_framework import serializers,fields
from .models import *


class ceva_details_serializer(serializers.ModelSerializer):        
    class Meta:
        model =CevaShipmentDetail
        fields='__all__'


 
    




 