from rest_framework import serializers


class ScientificDirectorSerializer(serializers.Serializer):
    pk = serializers.IntegerField()
    last_name = serializers.CharField(max_length=200)
    first_name = serializers.CharField(max_length=200)
    patronymic = serializers.CharField(max_length=200)


class StudentSerializer(serializers.Serializer):
    pk = serializers.IntegerField()
    last_name = serializers.CharField(max_length=200)
    first_name = serializers.CharField(max_length=200)
    patronymic = serializers.CharField(max_length=200)


class BachelorTopicSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=200)
    year = serializers.IntegerField()

    director = serializers.SerializerMethodField()
    students = serializers.SerializerMethodField()

    def get_director(self, obj):
        return ScientificDirectorSerializer(obj.director).data

    def get_students(self, obj):
        return StudentSerializer(obj.student_set.all(), many=True).data