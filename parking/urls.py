from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ParkViewSet

router = DefaultRouter(trailing_slash=False)
router.register("", ParkViewSet, basename="parking")

app_name = "parking"

urlpatterns = [
    path("", include(router.urls)),
]
