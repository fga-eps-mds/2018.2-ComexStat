import graphene

import comex_stat.assets.schema


class Query(comex_stat.assets.schema.Query, graphene.ObjectType):
    # This class will inherit from multiple Queries
    # as we begin to add more apps to our project
    class Meta:
        description = "Essas são as operações possíveis de pesquisa e os respectivos campos que elas podem retornar. Abaixo de cada uma pode ser encontrada uma breve descrição sobre a sua função"


schema = graphene.Schema(query=Query)
