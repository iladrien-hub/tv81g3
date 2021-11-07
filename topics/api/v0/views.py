from rest_framework.decorators import api_view, permission_classes
from rest_framework.generics import ListAPIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from topics.api.v0.serializers import BachelorTopicSerializer
from topics.models import BachelorTopic


@api_view(('GET',))
@permission_classes([AllowAny])
def ping(request):
    return Response(data={
        "message": "Hi there! Topics APIv0 up and running!"
    })


class ListTopics(ListAPIView):
    permission_classes = [AllowAny]
    queryset = BachelorTopic.objects.all()
    serializer_class = BachelorTopicSerializer
