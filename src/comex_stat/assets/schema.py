import graphene

from graphene_django.types import DjangoObjectType

from comex_stat.assets.models import AssetImportFacts, AssetExportFacts

class AssetImportFactsType(DjangoObjectType):
    class Meta:
        model = AssetImportFacts

class AssetExportFactsType(DjangoObjectType):
    class Meta:
        model = AssetExportFacts

class Query(object):
    all_import = graphene.List(AssetImportFactsType)
    all_export = graphene.List(AssetExportFactsType)

    def resolve_all_import(self, info, **kwargs):
        return AssetImportFacts.objects.all()

    def resolve_all_export(self, info, **kwargs):
        return AssetExportFacts.objects.all()
