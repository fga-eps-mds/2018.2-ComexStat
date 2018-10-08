import json
from datetime import datetime, time

import graphene
from comex_stat.assets.models import (CGCE, CUCI, NCM, SH, AssetExportFacts,
                                      AssetImportFacts, Country,
                                      FederativeUnit, TradeBlocs,
                                      Transportation, Urf)
from django_filters import rest_framework
from django.forms import DateField, Field
from django_filters.filters import RangeFilter
from django_filters.utils import handle_timezone
from graphene_django.filter.fields import DjangoFilterConnectionField
from graphene_django.types import DjangoObjectType


class DateRangeField(Field):

    def compress(self, data_list):
        if data_list:
            start_date, stop_date = data_list
            if start_date:
                start_date = handle_timezone(
                    datetime.combine(start_date, time.min))
            if stop_date:
                stop_date = handle_timezone(
                    datetime.combine(stop_date, time.max))
            return slice(start_date, stop_date)
        return None

    def clean(self, value):
        if value:
            clean_data = []
            values = json.loads(value)
            if isinstance(values, (list, tuple)):
                for field_value in values:
                    clean_data.append(DateField().clean(field_value))
            return self.compress(clean_data)
        else:
            return self.compress([])


class DateFromToRangeFilter(RangeFilter):
    field_class = DateRangeField


class AssetImpFilter(rest_framework.FilterSet):

    commercialized_between = DateFromToRangeFilter('date')

    class Meta:
        model = AssetImportFacts
        fields = ['commercialized_between', 'name']


class AssetImportFactsNode(DjangoObjectType):
    class Meta:
        # Assume you have an Animal model defined with the following fields
        model = AssetImportFacts
        filter_fields = ['commercialized_between', 'name']
        interfaces = (graphene.Node, )


class AssetExpFilter(rest_framework.FilterSet):

    commercialized_between = DateFromToRangeFilter('date')

    class Meta:
        model = AssetExportFacts
        fields = ['commercialized_between', 'name']


class AssetExportFactsNode(DjangoObjectType):
    class Meta:
        # Assume you have an Animal model defined with the following fields
        model = AssetExportFacts
        filter_fields = ['commercialized_between', 'name']
        interfaces = (graphene.Node, )


class AssetImportFactsType(DjangoObjectType):
    class Meta:
        model = AssetImportFacts
        filter_fields = {

            'date': ['icontains'],
            'name': ['icontains'],
            'registries': ['icontains'],
            'net_kilogram': ['icontains'],
            'fob_value': ['icontains']
        }
        interfaces = {graphene.Node, }


class AssetExportFactsType(DjangoObjectType):
    class Meta:
        model = AssetExportFacts
        filter_fields = {
            'date': ['icontains'],
            'name': ['icontains'],
            'registries': ['icontains'],
            'net_kilogram': ['icontains'],
            'fob_value': ['icontains']
        }
        interfaces = {graphene.Node, }


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


class TradeBlocsType(DjangoObjectType):
    class Meta:
        model = TradeBlocs
        filter_fields = {
            'name_portuguese': ['icontains'],
            'name_english': ['icontains'],
            'name_spanish': ['icontains'],
            'code': ['icontains']
        }
        interfaces = {graphene.Node, }


class CountryType(DjangoObjectType):
    class Meta:
        model = Country
        filter_fields = {
            'name_portuguese': ['icontains'],
            'name_english': ['icontains'],
            'name_spanish': ['icontains'],
            'code_iso3': ['icontains']
        }
        interfaces = {graphene.Node, }


class FederativeUnitType(DjangoObjectType):
    class Meta:
        model = FederativeUnit
        filter_fields = {
            'code': ['icontains'],
            'name': ['icontains'],
            'initials': ['icontains']
        }
        interfaces = {graphene.Node, }


class TransportationType(DjangoObjectType):
    class Meta:
        model = Transportation
        filter_fields = {
            'name': ['icontains'],
            'code': ['icontains']
        }
        interfaces = {graphene.Node, }


class UrfType(DjangoObjectType):
    class Meta:
        model = Urf
        filter_fields = {
            'code': ['icontains'],
            'name': ['icontains'],
        }
        interfaces = {graphene.Node, }


class Query(graphene.ObjectType):
    all_importsec = DjangoFilterConnectionField(AssetImportFactsNode,
                                                filterset_class=AssetImpFilter)
    all_exportsec = DjangoFilterConnectionField(AssetExportFactsNode,
                                                filterset_class=AssetExpFilter)
    all_import = DjangoFilterConnectionField(
        AssetImportFactsType)
    all_export = DjangoFilterConnectionField(AssetExportFactsType)
    all_tradeBlocs = DjangoFilterConnectionField(TradeBlocsType)
    all_country = DjangoFilterConnectionField(CountryType)
    all_federativeUnit = DjangoFilterConnectionField(FederativeUnitType)
    all_transportation = DjangoFilterConnectionField(TransportationType)
    all_urf = DjangoFilterConnectionField(UrfType)
    all_ncm = DjangoFilterConnectionField(NCMType)
    all_cuci = DjangoFilterConnectionField(CUCIType)
    all_cgce = DjangoFilterConnectionField(CGCEType)
    all_sh = DjangoFilterConnectionField(SHType)

    def resolve_all_import(self, info, **kwargs):
        return AssetImportFacts.objects.all()

    def resolve_all_importsec(self, info, **kwargs):
        return AssetImportFacts.objects.all()

    def resolve_all_exportsec(self, info, **kwargs):
        return AssetExportFacts.objects.all()

    def resolve_all_export(self, info, **kwargs):
        return AssetExportFacts.objects.all()

    def resolve_all_ncm(self, info, **kwargs):
        return NCM.objects.all()

    def resolve_all_tradeBlocs(self, info, **kwargs):
        return TradeBlocs.objects.all()

    def resolve_all_country(self, info, **kwargs):
        return Country.objects.all()

    def resolve_all_federativeUnit(self, info, **kwargs):
        return FederativeUnit.objects.all()

    def resolve_all_transportation(self, info, **kwargs):
        return Transportation.objects.all()

    def resolve_all_urf(self, info, **kwargs):
        return Urf.objects.all()

    def resolve_all_cuci(self, info, **kwargs):
        return CUCI.objects.all()

    def resolve_all_cgce(self, info, **kwargs):
        return CGCE.objects.all()

    def resolve_all_sh(self, info, **kwargs):
        return SH.objects.all()
