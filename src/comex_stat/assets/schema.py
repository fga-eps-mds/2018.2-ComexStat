import graphene

from graphene_django.types import DjangoObjectType

from comex_stat.assets.models import AssetImportFacts
from comex_stat.assets.models import AssetExportFacts
from comex_stat.assets.models import NCM
from comex_stat.assets.models import CUCI


class AssetImportFactsType(DjangoObjectType):
    class Meta:
        model = AssetImportFacts


class AssetExportFactsType(DjangoObjectType):
    class Meta:
        model = AssetExportFacts


class NCMType(DjangoObjectType):
    class Meta:
        model = NCM


class CUCIType(DjangoObjectType):
    class Meta:
        model = CUCI


class Query(object):
    all_import = graphene.List(AssetImportFactsType)
    all_export = graphene.List(AssetExportFactsType)
    all_ncm = graphene.List(NCMType)
    all_cuci = graphene.List(CUCIType)

    def resolve_all_import(self, info, **kwargs):
        return AssetImportFacts.objects.all()

    def resolve_all_export(self, info, **kwargs):
        return AssetExportFacts.objects.all()

    def resolve_all_ncm(self, info, **kwargs):
        return NCM.objects.all()

    def resolve_all_cuci(self, info, **kwargs):
        return CUCI.objects.all()
