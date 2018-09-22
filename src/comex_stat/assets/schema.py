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
            'ncm_code': ['icontains'],
            'ncm_name_pt': ['icontains'],
            'ncm_name_en': ['icontains'],
            'ncm_name_es': ['icontains'],
            'statistic_unit_code': ['icontains'],
            'ppe_code': ['icontains'],
            'ppi_code': ['icontains'],
            'aggregate_factor_code': ['icontains'],
            'cuci': [],
            'cgce': [],
            'sh': [],
            'isic4_code': ['icontains'],
            'exportation_subset': ['icontains'],
            'siit_code': ['icontains']
        }
        interfaces = {graphene.Node, }


class CUCIType(DjangoObjectType):
    class Meta:
        model = CUCI
        filter_fields = {
            'item_code': ['icontains'],
            'item_name_pt': ['icontains'],
            'item_name_en': ['icontains'],
            'item_name_es': ['icontains'],
            'subitem_code': ['icontains'],
            'subitem_name_pt': ['icontains'],
            'subitem_name_en': ['icontains'],
            'subitem_name_es': ['icontains'],
            'position_code': ['icontains'],
            'position_name_pt': ['icontains'],
            'position_name_en': ['icontains'],
            'position_name_es': ['icontains'],
            'chapter_code': ['icontains'],
            'chapter_name_pt': ['icontains'],
            'chapter_name_en': ['icontains'],
            'chapter_name_es': ['icontains'],
            'section_code': ['icontains'],
            'section_name_pt': ['icontains'],
            'section_name_en': ['icontains'],
            'section_name_es': ['icontains']
        }
        interfaces = {graphene.Node, }


class CGCEType(DjangoObjectType):
    class Meta:
        model = CGCE
        filter_fields = {
            'level1_code': ['icontains'],
            'level1_name_pt': ['icontains'],
            'level1_name_en': ['icontains'],
            'level1_name_es': ['icontains'],
            'level2_code': ['icontains'],
            'level2_name_pt': ['icontains'],
            'level2_name_en': ['icontains'],
            'level2_name_es': ['icontains'],
            'level3_code': ['icontains'],
            'level3_name_pt': ['icontains'],
            'level3_name_en': ['icontains'],
            'level3_name_es': ['icontains']
        }
        interfaces = {graphene.Node, }


class SHType(DjangoObjectType):
    class Meta:
        model = SH
        filter_fields = {
            'chapter_code': ['icontains'],
            'chapter_name_pt': ['icontains'],
            'chapter_name_en': ['icontains'],
            'chapter_name_es': ['icontains'],
            'position_code': ['icontains'],
            'position_name_pt': ['icontains'],
            'position_name_en': ['icontains'],
            'position_name_es': ['icontains'],
            'subposition_code': ['icontains'],
            'subposition_name_pt': ['icontains'],
            'subposition_name_en': ['icontains'],
            'subposition_name_es': ['icontains'],
            'section_code': ['icontains'],
            'section_name_pt': ['icontains'],
            'section_name_en': ['icontains'],
            'section_name_es': ['icontains']
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
