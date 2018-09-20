import graphene

from graphene_django.types import DjangoObjectType

from comex_stat.assets.models import AssetImportFacts
from comex_stat.assets.models import AssetExportFacts
from comex_stat.assets.models import NCM
from comex_stat.assets.models import CUCI
from comex_stat.assets.models import CGCE
from comex_stat.assets.models import SH


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


class CGCEType(DjangoObjectType):
    class Meta:
        model = CGCE


class SHType(DjangoObjectType):
    class Meta:
        model = SH


class Query(object):
    all_import = graphene.List(AssetImportFactsType)
    all_export = graphene.List(AssetExportFactsType)
    all_ncm = graphene.List(NCMType)
    all_cuci = graphene.List(CUCIType)
    all_cgce = graphene.List(CGCEType)
    all_sh = graphene.List(SHType)

    def resolve_all_import(self, info, **kwargs):
        return AssetImportFacts.objects.all()

    def resolve_all_export(self, info, **kwargs):
        return AssetExportFacts.objects.all()

    def resolve_all_ncm(self, info, **kwargs):
        return NCM.objects.all()

    def resolve_all_cuci(self, info, **kwargs):
        return CUCI.objects.all()

    def resolve_all_cgce(self, info, **kwargs):
        return CGCE.objects.all()

    def resolve_all_sh(self, info, **kwargs):
        return SH.objects.all()
