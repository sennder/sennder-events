from rest_framework import serializers


class EventSerializer(serializers.Serializer):

    ID = serializers.CharField()
    properties = serializers.JSONField()
    signature = serializers.JSONField()
