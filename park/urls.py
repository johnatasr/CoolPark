from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ParkViewSet

routes = {
        "check_in": 'parking',
        "check_out": 'parking/(?P<id>[0-9]+)/out',
        "do_payment": 'parking/(?P<id>[0-9]+)/pay',
        "parking_history": 'parking/(?P<plate>[A-Z]{3}-[0-9]{4})'
        }

router = DefaultRouter(trailing_slash=False)
router.register('', ParkViewSet, basename='parking')

app_name = 'park'

urlpatterns = [
    path('', include(router.urls)),
]

