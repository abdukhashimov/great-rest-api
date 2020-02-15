from django.urls import path
from rest_framework.routers import DefaultRouter
from info.views import InfoViewSet

router = DefaultRouter()

router.register('info', InfoViewSet)

urlpatterns = router.urls
