import graphene

from graphene_django.types import DjangoObjectType

from comex_stat.assets.models import AssetImportFacts, AssetExportFacts

class AssetImportFactsType(DjangoObjectType):
    class Meta:
        model = AssetImportFacts

class Query(object):
    all_import = graphene.List(AssetImportFactsType)

    def resolve_all_import(self, info, **kwargs):
        return AssetImportFacts.objects.all()
