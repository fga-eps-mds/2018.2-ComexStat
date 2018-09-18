import graphene

import comex_stat.assets.schema


class Query(comex_stat.assets.schema.Query, graphene.ObjectType):
    # This class will inherit from multiple Queries
    # as we begin to add more apps to our project
    pass

schema = graphene.Schema(query=Query)
