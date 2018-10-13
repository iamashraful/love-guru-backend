from rest_framework import serializers


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField(required=True, max_length=32)
    password = serializers.CharField(required=True, max_length=32)
