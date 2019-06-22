import graphene
from graphene import InputObjectType


class UserInput(InputObjectType):
    username = graphene.String()
    password = graphene.String()
    confirm_password = graphene.String()


class ProfileInput(InputObjectType):
    name = graphene.String()
    address = graphene.String()
    phone = graphene.String()
    gender = graphene.String()
    created_at = graphene.DateTime()
    updated_at = graphene.DateTime()
    is_active = graphene.Boolean()
    user = graphene.Field(UserInput)
