from rest_framework import routers
from .api import ProjectViewSet

router = routers.DefaultRouter()

router.register('api/projects',ProjectViewSet,'projects')      #genera 4 ULS  al utilizar register que son POST, Delete,Get,Update en un asola url

urlpatterns = router.urls