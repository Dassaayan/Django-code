from django.conf.urls import url
from rest_framework import routers
from ceva_shipment_api_design.views import *

router = routers.DefaultRouter()
router.register(r'details',cevaapiView)
#router.register(r'details',coscoView)

urlpatterns = router.urls
