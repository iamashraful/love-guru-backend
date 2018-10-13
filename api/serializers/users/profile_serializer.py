from rest_framework.serializers import ModelSerializer

from api.models import Profile


class ProfileSerializer(ModelSerializer):
    class Meta:
        model = Profile
        fields = ('user', 'user__username', 'name', 'phone', 'address', 'gender', 'photo',)
