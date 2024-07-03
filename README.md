# GraphQL 
+ GraphQL is an open-source data query language for APIs and It is a server-side runtime for executing the query. The server’s GraphQL runtime takes care of executing the query and ensuring that the right data is fetched and sent back.

+  It is an alternative to REST, where clients make multiple requests to different endpoints to get the data they require but in GraphQL clients can request exactly the data they need in a single query.

   It was developed by Facebook and made open source for the whole world.


### Graphene-Django

Graphene-Django is an open-source library that provides seamless integration between Django, a high-level Python web framework, and Graphene, a library for building GraphQL APIs. The library allows developers to create GraphQL APIs in Django quickly and efficiently while maintaining a high level of performance.

### Installation
To install Graphene-Django, run the following command:
```
pip install graphene-django
```
### Configuration
After installation, add 'graphene_django' to your Django project's INSTALLED_APPS list and define the GraphQL schema in your project's settings:
```
INSTALLED_APPS = [
    # ...
    'graphene_django',
]

GRAPHENE = {
    'SCHEMA': 'myapp.schema.schema'
}
```
### Usage
To use Graphene-Django, create a schema.py file in your Django app directory and define your GraphQL types and queries:
```
import graphene
from graphene_django import DjangoObjectType
from .models import MyModel

class MyModelType(DjangoObjectType):
    class Meta:
        model = MyModel

class Query(graphene.ObjectType):
    mymodels = graphene.List(MyModelType)

    def resolve_mymodels(self, info, **kwargs):
        return MyModel.objects.all()

schema = graphene.Schema(query=Query)
Then, expose the GraphQL API in your Django project's urls.py file:

from django.urls import path
from graphene_django.views import GraphQLView
from . import schema

urlpatterns = [
    # ...
    path('graphql/', GraphQLView.as_view(graphiql=True)), # Given that schema path is defined in GRAPHENE['SCHEMA'] in your settings.py
]

```
### Testing
Graphene-Django provides support for testing GraphQL APIs using Django's test client. To create tests, create a tests.py file in your Django app directory and write your test cases:
```
from django.test import TestCase
from graphene_django.utils.testing import GraphQLTestCase
from . import schema

class MyModelAPITestCase(GraphQLTestCase):
    GRAPHENE_SCHEMA = schema.schema

    def test_query_all_mymodels(self):
        response = self.query(
            '''
            query {
                mymodels {
                    id
                    name
                }
            }
            '''
        )

        self.assertResponseNoErrors(response)
        self.assertEqual(len(response.data['mymodels']), MyModel.objects.count())
```
