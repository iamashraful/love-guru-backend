import graphene
from graphene import InputObjectType


class UserSchema(InputObjectType):
    id = graphene.ID()
    username = graphene.String()
    first_name = graphene.String()
    last_name = graphene.String()
    is_active = graphene.Boolean()


class ProfileSchema(InputObjectType):
    id = graphene.ID()
    name = graphene.String()
    address = graphene.String()
    phone = graphene.String()
    gender = graphene.String()
    created_at = graphene.DateTime()
    updated_at = graphene.DateTime()
    is_active = graphene.Boolean()
