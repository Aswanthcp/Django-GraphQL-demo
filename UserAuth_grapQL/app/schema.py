import graphene
import graphql_jwt
from graphql_auth.schema import UserQuery, MeQuery
from graphql_auth import mutations


class AuthMutation(graphene.ObjectType):
    register = mutations.Register.Field()
    verify_account = mutations.VerifyAccount.Field()
    token_auth = mutations.ObtainJSONWebToken.Field()
    update_account = mutations.UpdateAccount.Field()


class Query(UserQuery, MeQuery, graphene.ObjectType):
    pass


schema = graphene.Schema(query=Query, mutation=AuthMutation)
