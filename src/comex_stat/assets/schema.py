import graphene

from graphene_django.types import DjangoObjectType
from graphene_django.filter.fields import DjangoFilterConnectionField


from comex_stat.assets.models import (AssetImportFacts, AssetExportFacts,
                                      NCM, CUCI, CGCE, SH)


class AssetImportFactsType(DjangoObjectType):
    class Meta:
        model = AssetImportFacts


class AssetExportFactsType(DjangoObjectType):
    class Meta:
        model = AssetExportFacts


class NCMType(DjangoObjectType):
    class Meta:
        model = NCM
        filter_fields = {
            'ncm': ['icontains'],
            'unid': ['icontains'],
            'ppe': ['icontains'],
            'ppi': ['icontains'],
            'fat_agreg': ['icontains'],
            'cuci': [],
            'isic4': ['icontains'],
            'cgce': [],
            'sh': [],
            'exp_subset': ['icontains'],
            'ncm_pt': ['icontains'],
            'ncm_en': ['icontains'],
            'ncm_es': ['icontains'],
            'siit': ['icontains']
        }
        interfaces = {graphene.Node, }


class CUCIType(DjangoObjectType):
    class Meta:
        model = CUCI
        filter_fields = {
            'cuci_item': ['icontains'],
            'cuci_item_pt': ['icontains'],
            'cuci_item_en': ['icontains'],
            'cuci_item_es': ['icontains'],
            'cuci_sub': ['icontains'],
            'cuci_sub_pt': ['icontains'],
            'cuci_sub_en': ['icontains'],
            'cuci_sub_es': ['icontains'],
            'cuci_pos': ['icontains'],
            'cuci_pos_pt': ['icontains'],
            'cuci_pos_en': ['icontains'],
            'cuci_pos_es': ['icontains'],
            'cuci_cap': ['icontains'],
            'cuci_cap_pt': ['icontains'],
            'cuci_cap_en': ['icontains'],
            'cuci_cap_es': ['icontains'],
            'cuci_sec': ['icontains'],
            'cuci_sec_pt': ['icontains'],
            'cuci_sec_en': ['icontains'],
            'cuci_sec_es': ['icontains']
        }
        interfaces = {graphene.Node, }


class CGCEType(DjangoObjectType):
    class Meta:
        model = CGCE
        filter_fields = {
            'cgce_n1': ['icontains'],
            'cgce_n1_pt': ['icontains'],
            'cgce_n1_en': ['icontains'],
            'cgce_n1_es': ['icontains'],
            'cgce_n2': ['icontains'],
            'cgce_n2_pt': ['icontains'],
            'cgce_n2_en': ['icontains'],
            'cgce_n2_es': ['icontains'],
            'cgce_n3': ['icontains'],
            'cgce_n3_pt': ['icontains'],
            'cgce_n3_en': ['icontains'],
            'cgce_n3_es': ['icontains']
        }
        interfaces = {graphene.Node, }


class SHType(DjangoObjectType):
    class Meta:
        model = SH
        filter_fields = {
            'sh2': ['icontains'],
            'sh2_pt': ['icontains'],
            'sh2_en': ['icontains'],
            'sh2_es': ['icontains'],
            'sh4': ['icontains'],
            'sh4_pt': ['icontains'],
            'sh4_en': ['icontains'],
            'sh4_es': ['icontains'],
            'sh6': ['icontains'],
            'sh6_pt': ['icontains'],
            'sh6_en': ['icontains'],
            'sh6_es': ['icontains'],
            'ncm_secrom': ['icontains'],
            'sec_pt': ['icontains'],
            'sec_en': ['icontains'],
            'sec_es': ['icontains']
        }
        interfaces = {graphene.Node, }


class Query(object):
    all_import = graphene.List(AssetImportFactsType)
    all_export = graphene.List(AssetExportFactsType)
    all_ncm = DjangoFilterConnectionField(NCMType)
    all_cuci = DjangoFilterConnectionField(CUCIType)
    all_cgce = DjangoFilterConnectionField(CGCEType)
    all_sh = DjangoFilterConnectionField(SHType)

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
