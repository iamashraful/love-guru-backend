from rest_framework.generics import ListAPIView

from api.models import Profile
from api.serializers.users.profile_serializer import ProfileSerializer


class ProfileListView(ListAPIView):
    serializer_class = ProfileSerializer
    queryset = Profile.objects.filter(user__is_active=True)
