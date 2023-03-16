from rest_framework.views import APIView
from .serializers import PingPongSerializer
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
