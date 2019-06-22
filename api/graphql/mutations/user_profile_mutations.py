import graphene
from django.contrib.auth.models import User

from api.graphql.schema.user_profile_schema import ProfileInput
from api.graphql.types.user_profile_type import ProfileType, UserType
from api.models import Profile


class CreateUserProfile(graphene.Mutation):
    class Arguments:
        input = ProfileInput(required=True)

    success = graphene.Boolean()
    profile = graphene.Field(ProfileType)

    @staticmethod
    def mutate(root, info, input=None):
        success = True
        _user = input.user
        _password = _user.get('password', '')
        _confirm_password = _user.get('confirm_password', '')
        if _password == _confirm_password:
            _u = User(username=_user.get('username'))
            _u.save()
            _u.set_password(_password)
        else:
            raise Exception('password and confirm password should match')
        _instance = Profile(user=_u, name=input.name, address=input.address, phone=input.phone, gender=input.gender)
        _instance.save()
        return CreateUserProfile(success=success, profile=_instance)
