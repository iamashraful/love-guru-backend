from rest_framework.authtoken.models import Token
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from api.serializers.users.auth_serializers import LoginSerializer


class LoginView(APIView):
    permission_classes = (AllowAny,)

    def post(self, request, *args, **kwargs):
        _data = request.data
        _serializer = LoginSerializer(data=_data)
        if _serializer.is_valid(raise_exception=True):
            _user = _serializer.login_validator(_data)
            if _user is not None:
                token, _created = Token.objects.get_or_create(user_id=_user.pk)
                response = {
                    "token": token.key,
                    "username": _user.username
                }
                return Response(response)
        return Response({})
