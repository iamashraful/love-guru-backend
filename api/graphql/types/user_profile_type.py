import graphene
from django.contrib.auth.models import User
from graphene import ObjectType
from graphene_django import DjangoObjectType

from api.models import Profile


class UserType(DjangoObjectType):
    class Meta:
        model = User


class ProfileType(DjangoObjectType):
    class Meta:
        model = Profile


# Creating query type
class Query(ObjectType):
    user = graphene.Field(UserType, id=graphene.Int())
    profile = graphene.Field(ProfileType, id=graphene.Int())

    users = graphene.List(UserType)
    profiles = graphene.List(ProfileType)

    def resolve_user(self, info, **kwargs):
        _id = kwargs.get('id')
        if _id:
            return User.objects.get(pk=_id)

    def resolve_profile(self, info, **kwargs):
        _id = kwargs.get('id')
        if _id:
            return Profile.objects.get(pk=_id)

    def resolve_users(self, info, **kwargs):
        return User.objects.all()

    def resolve_profiles(self, info, **kwargs):
        return Profile.objects.all()
