from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ParkViewSet

router = DefaultRouter(trailing_slash=True)

router.register('parking', ParkViewSet.check_in, basename='parking')
router.register('parking/<id:int>/out', ParkViewSet.check_out, basename='parking')
router.register('parking/<id:int>/pay', ParkViewSet.do_payment, basename='parking')
router.register('parking/<plate:str>', ParkViewSet.parking_history, basename='parking')

app_name = 'park'

urlpatterns = [
    path('', include(router.urls)),
]