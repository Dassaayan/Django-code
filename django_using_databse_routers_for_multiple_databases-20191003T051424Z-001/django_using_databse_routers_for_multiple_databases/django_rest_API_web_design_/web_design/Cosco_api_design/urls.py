from django.conf.urls import url
from rest_framework import routers
from Cosco_api_design.views import *

router = routers.DefaultRouter()
router.register(r'details',coscoapiView)

urlpatterns = router.urls