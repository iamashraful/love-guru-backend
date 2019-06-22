import graphene

from api.graphql.schema.user_profile_schema import ProfileInput
from api.graphql.types.user_profile_type import ProfileType, UserType
from api.models import Profile


class CreateUserProfile(graphene.Mutation):
    class Arguments:
        input = ProfileInput(required=True)

    success = graphene.Boolean()
    # user = graphene.Field(UserType)
    profile = graphene.Field(ProfileType)

    @staticmethod
    def mutate(root, info, input=None):
        success = True
        _instance = Profile(name=input.name, address=input.address, phone=input.phone, gender=input.gender)
        _instance.save()
        return CreateUserProfile(status=success, profile=_instance)
