from rest_framework import serializers


class EventSerializer(serializers.Serializer):

    ID = serializers.CharField()
    properties = serializers.DictField()
    signature = serializers.DictField()
