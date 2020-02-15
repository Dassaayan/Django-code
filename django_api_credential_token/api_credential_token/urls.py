from django.conf.urls import url
from rest_framework import routers
from api_credential_token.views import *

router = routers.DefaultRouter()
router.register(r'details',employeeViewSet)
# router.register(r'employee/details',employeeFilteredViewSet)
 
urlpatterns = router.urls