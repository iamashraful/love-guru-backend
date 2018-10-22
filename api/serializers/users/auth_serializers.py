from django.contrib.auth import authenticate
from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from api.models import Profile


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField(required=True, max_length=32)
    password = serializers.CharField(required=True, max_length=32)

    def login_validator(self, attrs):
        _username = attrs.get('username')
        _users = Profile.objects.filter(user__username__iexact=_username)
        if _users.exists() and _users.count() == 1:
            _password = attrs.get('password')
            _current_user = authenticate(username=_username, password=_password)
            if _current_user is not None:
                return _current_user
        raise ValidationError({'success': False, 'message': 'Login credentials are incorrect.'})
