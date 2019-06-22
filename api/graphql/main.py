import graphene

from api.graphql.mutations.main import Mutation
from api.graphql.types.user_profile_type import Query


class MainQuery(Query, graphene.ObjectType):
    pass


class MainMutation(Mutation, graphene.ObjectType):
    pass


schema = graphene.Schema(query=MainQuery, mutation=MainMutation)
