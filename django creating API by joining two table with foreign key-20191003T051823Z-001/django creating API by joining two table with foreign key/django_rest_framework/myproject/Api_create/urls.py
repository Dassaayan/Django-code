from django.conf.urls import url
from rest_framework import routers
from Api_create.views import movieViewSet,MovieFilteredViewSet#,MovieFilteredViewSet_credits

router = routers.DefaultRouter()
router.register(r'details',movieViewSet)
router.register(r'/Movie/details',MovieFilteredViewSet)
#router.register(r'/credits',MovieFilteredViewSet_credits)
 
urlpatterns = router.urls