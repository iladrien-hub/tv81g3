from rest_framework import serializers


class BachelorTopicSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=200)
