# Demo using GraphQL 

This is a demo project to show how to use GraphQL with Django and  python library graphene  for GraphQL

first we need to install python library graphene ,
```
pip install graphene-django

```


input query in QraphQl interface - 
```
query getBookquery{
    books {
        id
        title
    }
}
```
