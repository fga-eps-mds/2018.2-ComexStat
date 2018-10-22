import json
from datetime import datetime, time

import graphene
from comex_stat.assets.models import (CGCE, CUCI, NCM, SH, AssetExportFacts,
                                      AssetImportFacts, Country,
                                      FederativeUnit, TradeBlocs,
                                      Transportation, Urf)

from django_filters import FilterSet, CharFilter
from django.forms import DateField, Field
from django_filters.filters import RangeFilter
from django_filters.utils import handle_timezone
from graphene_django.filter.fields import DjangoFilterConnectionField
from graphene_django.types import DjangoObjectType


class DateRangeField(Field):

    '''

        Class that expects to receive a JSON string,
        like: "[\"yyyy-mm-dd\",\"yyyy-mm-dd\"]"
        The first date being the begin and the second the end.
        The function then splits the two dates into DateFields
        and interprets the range between them by using datetime functions.

    '''

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
    '''
     Class to define cutom field-filter that will use the DateRange function.

    '''

    field_class = DateRangeField


class AssetImportFilter(FilterSet):

    '''
     Custom filter-set class for Import facts
    '''

    # temporary field used to filter date fields by range
    commercialized_between = DateFromToRangeFilter('date')
    date = CharFilter(
        field_name="date", lookup_expr="icontains")
    registries = CharFilter(
        field_name="registries", lookup_expr="icontains")
    net_kilogram = CharFilter(
        field_name="net_kilogram", lookup_expr="icontains")
    fob_value = CharFilter(
        field_name="fob_value", lookup_expr="icontains")

    class Meta:
        model = AssetImportFacts
        fields = ['commercialized_between',
                  'date', 'registries', 'net_kilogram', 'fob_value']


class AssetExportFilter(FilterSet):

    '''
     Custom filter-set class for Export facts
    '''

    # temporary field used to filter date fields by range
    commercialized_between = DateFromToRangeFilter('date')
    date = CharFilter(
        field_name="date", lookup_expr="icontains")
    registries = CharFilter(
        field_name="registries", lookup_expr="icontains")
    net_kilogram = CharFilter(
        field_name="net_kilogram", lookup_expr="icontains")
    fob_value = CharFilter(
        field_name="fob_value", lookup_expr="icontains")

    class Meta:
        model = AssetExportFacts
        fields = ['commercialized_between',
                  'date', 'registries', 'net_kilogram', 'fob_value']


class AssetImportFactsNode(DjangoObjectType):
    class Meta:
        model = AssetImportFacts
        filter_fields = ['commercialized_between',
                         'date', 'registries', 'net_kilogram', 'fob_value']
        interfaces = (graphene.Node, )


class AssetExportFactsNode(DjangoObjectType):
    class Meta:
        model = AssetExportFacts
        filter_fields = ['commercialized_between',
                         'date', 'registries', 'net_kilogram', 'fob_value']
        interfaces = (graphene.Node, )


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


class TradeBlocsType(DjangoObjectType):
    class Meta:
        model = TradeBlocs
        filter_fields = {
            'bloc_name_pt': ['icontains'],
            'bloc_name_en': ['icontains'],
            'bloc_name_es': ['icontains'],
            'bloc_code': ['icontains']
        }
        interfaces = {graphene.Node, }


class CountryType(DjangoObjectType):
    class Meta:
        model = Country
        filter_fields = {
            'country_name_pt': ['icontains'],
            'country_name_en': ['icontains'],
            'country_name_es': ['icontains'],
            'country_code_iso3': ['icontains']
        }
        interfaces = {graphene.Node, }


class FederativeUnitType(DjangoObjectType):
    class Meta:
        model = FederativeUnit
        filter_fields = {
            'uf_code': ['icontains'],
            'uf_name': ['icontains'],
            'uf_initials': ['icontains']
        }
        interfaces = {graphene.Node, }


class TransportationType(DjangoObjectType):
    class Meta:
        model = Transportation
        filter_fields = {
            'transportation_name': ['icontains'],
            'transportation_code': ['icontains']
        }
        interfaces = {graphene.Node, }


class UrfType(DjangoObjectType):
    class Meta:
        model = Urf
        filter_fields = {
            'urf_code': ['icontains'],
            'urf_name': ['icontains'],
        }
        interfaces = {graphene.Node, }


class Query(graphene.ObjectType):
    all_import = DjangoFilterConnectionField(
        AssetImportFactsNode, filterset_class=AssetImportFilter)
    all_export = DjangoFilterConnectionField(
        AssetExportFactsNode, filterset_class=AssetExportFilter)
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
