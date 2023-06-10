from rest_framework import serializers

class GetAuthURLSerializer(serializers.Serializer):
    url = serializers.URLField()

class GetAccessTockenSerializer(serializers.Serializer):
    code = serializers.CharField(max_length=200)
