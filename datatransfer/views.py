from rest_framework import status, generics
from rest_framework.views import APIView

from .models import Purchase
from .serializers import PingPongSerializer, PurchaseSerializer
from rest_framework.response import Response


class PingPongView(APIView):
    @staticmethod
    def get(request):
        serializer = PingPongSerializer(data=request.GET)
        if serializer.is_valid():
            if serializer.data['ping'] == 'ping':
                return Response({'result': 'pong'})
            else:
                return Response({'result': 'What the hell?'})
        else:
            return Response('Wrong')


class PurchaseListAPIView(generics.ListAPIView):
    queryset = Purchase.objects.all()
    serializer_class = PurchaseSerializer

