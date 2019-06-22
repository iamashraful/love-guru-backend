from graphene import ObjectType

from api.graphql.mutations.user_profile_mutations import CreateUserProfile


class Mutation(ObjectType):
    create_user_profile = CreateUserProfile.Field()
