import graphene
from graphene_django import DjangoObjectType
from .models import Books


class BooksType(DjangoObjectType):
    class Meta:
        model = Books
        fields = ("id", "title", "excerpt")


class Query(graphene.ObjectType):
    books = graphene.List(BooksType)

    def resolve_books(self, info, **kwargs):
        return Books.objects.all()


schema = graphene.Schema(query=Query)
