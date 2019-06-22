from django.conf.urls import url
from rest_framework import routers
from poll.views import personViewSet

router = routers.DefaultRouter()
router.register(r'details', personViewSet)

 
urlpatterns = router.urls