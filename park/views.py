# Create your views here.
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.status import (
    HTTP_200_OK,
    HTTP_422_UNPROCESSABLE_ENTITY,
    HTTP_406_NOT_ACCEPTABLE,
    HTTP_400_BAD_REQUEST
)
from rest_framework.response import Response
from park.factories import ParkFactory


# Register your viewsets here.
class ParkViewSet(viewsets.GenericViewSet):
    """
       API usando Django RestFramework
    """
    factory = ParkFactory()
    http_method_names = ['get', 'post', 'put']

    @action(methods=['POST'], detail=False, url_path='parking')
    def check_in(self, request):
        """
            Check-in enpoint
        """
        try:
            check_in_result = self.factory.create_check_in_interator(data=request.data)
            return Response(check_in_result, status=HTTP_200_OK)
        except Exception as error:
            return Response({"msg": error.args[0]}, status=HTTP_400_BAD_REQUEST)

    @action(methods=['PUT'], detail=False, url_path='parking/(?P<id>[0-9]+)/out')
    def check_out(self, request, id):
        """
            Enpoint principal
        """
        try:
            check_out_result = self.factory.create_check_out_interator(id=id)
            return Response(check_out_result, status=HTTP_200_OK)
        except Exception as error:
            return Response(status=HTTP_422_UNPROCESSABLE_ENTITY)

    @action(methods=['PUT'], detail=False, url_path='parking/(?P<id>[0-9]+)/pay')
    def do_payment(self, request, id):
        """
            Enpoint principal
        """
        try:
            payment_result = self.factory.create_do_payment_interator(id=id)
            return Response(payment_result, status=HTTP_200_OK)
        except Exception as error:
            return Response(status=HTTP_422_UNPROCESSABLE_ENTITY)

    @action(methods=['GET'], detail=False, url_path='parking/(?P<plate>[A-Z]{3}-[0-9]{4})')
    def parking_history(self, request, plate: str):
        """
            Enpoint principal
        """
        try:
            history_result = self.factory.create_historic_interator(plate=plate)
            return Response(history_result, status=HTTP_200_OK)
        except Exception as error:
            return Response(status=HTTP_422_UNPROCESSABLE_ENTITY)