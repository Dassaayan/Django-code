from django.urls import include, path
from django.conf.urls import url
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router1=router.register(r'ShowtimePrograms/db', views.ShowtimeProgramsViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    url('', include(router.urls)),
    path(r'api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
