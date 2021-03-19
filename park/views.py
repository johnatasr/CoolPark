# Create your views here.
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.status import (
    HTTP_200_OK,
    HTTP_422_UNPROCESSABLE_ENTITY
)
from rest_framework.response import Response
from .factories import ParkFactory


# Register your viewsets here.
class ParkViewSet(viewsets.ViewSet):
    """
       API usando Django RestFramework
    """
    factory = ParkFactory()
    http_method_names = ['get', 'post', 'update']

    #@action(methods=['POST'], detail=False, url_path='check-in', url_name='check_in')
    @action(methods=['POST'], detail=False)
    def check_in(self, request):
        """
            Check-in enpoint
        """
        try:
            check_in_result = self.factory.create_check_in_interator(data=request.data)
            return Response(check_in_result, status=HTTP_200_OK)
        except Exception as error:
            return Response(status=HTTP_422_UNPROCESSABLE_ENTITY)

    #@action(methods=['UPDATE'], detail=False, url_path='check-in', url_name='check_in')
    @action(methods=['UPDATE'], detail=False)
    def check_out(self, request):
        """
            Enpoint principal
        """
        try:
            check_out_result = self.factory.create_check_out_interator(request.query_params.get('id'))
            return Response(check_out_result, status=HTTP_200_OK)
        except Exception as error:
            return Response(status=HTTP_422_UNPROCESSABLE_ENTITY)

    #@action(methods=['UPDATE'], detail=False, url_path='check_in', url_name='check_in')
    @action(methods=['UPDATE'], detail=False)
    def do_payment(self, request):
        """
            Enpoint principal
        """
        try:
            payment_result = self.factory.do_payment_interator(request.query_params.get('id'))
            return Response(payment_result, status=HTTP_200_OK)
        except Exception as error:
            return Response(status=HTTP_422_UNPROCESSABLE_ENTITY)

    #@action(methods=['GET'], detail=False, url_path='check_in', url_name='check_in')
    @action(methods=['GET'], detail=False)
    def parking_history(self, request):
        """
            Enpoint principal
        """
        try:
            history_result = self.factory.historic_interator(request.query_params.get('plate'))
            return Response(history_result, status=HTTP_200_OK)
        except Exception as error:
            return Response(status=HTTP_422_UNPROCESSABLE_ENTITY)