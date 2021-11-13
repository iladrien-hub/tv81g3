from rest_framework.decorators import api_view, permission_classes
from rest_framework.generics import ListAPIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from topics.api.v0.serializers import BachelorTopicSerializer
from topics.errors import BadRequest
from topics.models import BachelorTopic


@api_view(('GET',))
@permission_classes([AllowAny])
def ping(request):
    return Response(data={
        "message": "Hi there! Topics APIv0 up and running!"
    })


class ListTopics(ListAPIView):
    permission_classes = [AllowAny]
    serializer_class = BachelorTopicSerializer

    def get_queryset(self):
        queryset = list(BachelorTopic.objects.all())

        title: str = self.request.query_params.get('title')
        if title:
            title = title.lower()
            queryset = list(filter(lambda x: title in x.title.lower(), queryset))

        year = self.request.query_params.get('year')
        if year:
            try:
                year = int(year)
            except ValueError:
                raise BadRequest({
                    "year": f"Value \"{year}\" can't be interpreted as integer."
                })
            queryset = list(filter(lambda x: year == x.year, queryset))

        return queryset