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

    """
     Custom filter-set class for Import facts
    """

    # temporary field used to filter date fields by range
    commercialized_between = DateFromToRangeFilter('date')
    date = CharFilter(
        field_name="date", lookup_expr="icontains")
    registries = CharFilter(
        field_name="registries", lookup_expr="iexact")
    net_kilogram = CharFilter(
        field_name="net_kilogram", lookup_expr="iexact")
    fob_value = CharFilter(
        field_name="fob_value", lookup_expr="iexact")
    country_name_pt = CharFilter(
        field_name="origin_country__country_name_pt",
        lookup_expr="iexact")
    country_name_en = CharFilter(
        field_name="origin_country__country_name_en",
        lookup_expr="iexact")
    country_name_es = CharFilter(
        field_name="origin_country__country_name_es",
        lookup_expr="iexact")
    country_code_iso3 = CharFilter(
        field_name="origin_country__country_code_iso3",
        lookup_expr="iexact")
    trade_bloc_name_pt = CharFilter(
        field_name="origin_country__trade_bloc__bloc_name_pt",
        lookup_expr="iexact")
    trade_bloc_name_en = CharFilter(
        field_name="origin_country__trade_bloc__bloc_name_en",
        lookup_expr="iexact")
    trade_bloc_name_es = CharFilter(
        field_name="origin_country__trade_bloc__bloc_name_es",
        lookup_expr="iexact")
    trade_bloc_code = CharFilter(
        field_name="origin_country__trade_bloc__bloc_code",
        lookup_expr="iexact")
    federative_unity_name = CharFilter(
        field_name="destination_fed_unit__uf_name",
        lookup_expr="iexact")
    federative_unity_code = CharFilter(
        field_name="destination_fed_unit__uf_code",
        lookup_expr="iexact")
    federative_unity_initials = CharFilter(
        field_name="destination_fed_unit__uf_initials",
        lookup_expr="iexact")
    urf_name = CharFilter(
        field_name="urf__urf_name", lookup_expr="iexact")
    urf_code = CharFilter(
        field_name="urf__urf_code", lookup_expr="iexact")
    transportation_name = CharFilter(
        field_name="transportation__transportation_name",
        lookup_expr="iexact")
    transportation_code = CharFilter(
        field_name="transportation__transportation_code",
        lookup_expr="iexact")
    ncm_code = CharFilter(
        field_name="ncm__ncm_code",
        lookup_expr="iexact")
    statistic_unit_code = CharFilter(
        field_name="ncm__statistic_unit_code",
        lookup_expr="iexact")
    ppe_code = CharFilter(
        field_name="ncm__ppe_code",
        lookup_expr="iexact")
    ppi_code = CharFilter(
        field_name="ncm__ppi_code",
        lookup_expr="iexact")
    aggregate_factor_code = CharFilter(
        field_name="ncm__aggregate_factor_code",
        lookup_expr="iexact")
    isic4_code = CharFilter(
        field_name="ncm__isic4_code",
        lookup_expr="iexact")
    exportation_subset = CharFilter(
        field_name="ncm__exportation_subset",
        lookup_expr="iexact")
    siit_code = CharFilter(
        field_name="ncm__siit_code",
        lookup_expr="iexact")
    cuci_item_code = CharFilter(
        field_name="ncm__cuci__item_code",
        lookup_expr="iexact")
    cuci_subitem_code = CharFilter(
        field_name="ncm__cuci__subitem_code",
        lookup_expr="iexact")
    cuci_position_code = CharFilter(
        field_name="ncm__cuci__position_code",
        lookup_expr="iexact")
    cuci_chapter_code = CharFilter(
        field_name="ncm__cuci__chapter_code",
        lookup_expr="iexact")
    cuci_section_code = CharFilter(
        field_name="ncm__cuci__section_code",
        lookup_expr="iexact")
    cgce_level1_code = CharFilter(
        field_name="ncm__cgce__level1_code",
        lookup_expr="iexact"
    )
    cgce_level2_code = CharFilter(
        field_name="ncm__cgce__level2_code",
        lookup_expr="iexact"
    )
    cgce_level3_code = CharFilter(
        field_name="ncm__cgce__level3_code",
        lookup_expr="iexact"
    )
    sh_chapter_code = CharFilter(
        field_name="ncm__sh__chapter_code",
        lookup_expr="iexact"
    )
    sh_position_code = CharFilter(
        field_name="ncm__sh__position_code",
        lookup_expr="iexact"
    )
    sh_subposition_code = CharFilter(
        field_name="ncm__sh__subposition_code",
        lookup_expr="iexact"
    )
    sh_section_code = CharFilter(
        field_name="ncm__sh__section_code",
        lookup_expr="iexact"
    )

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
        field_name="registries", lookup_expr="iexact")
    net_kilogram = CharFilter(
        field_name="net_kilogram", lookup_expr="iexact")
    fob_value = CharFilter(
        field_name="fob_value", lookup_expr="iexact")
    country_name_pt = CharFilter(
        field_name="destination_country__country_name_pt",
        lookup_expr="iexact")
    country_name_en = CharFilter(
        field_name="destination_country__country_name_en",
        lookup_expr="iexact")
    country_name_es = CharFilter(
        field_name="destination_country__country_name_es",
        lookup_expr="iexact")
    country_code_iso3 = CharFilter(
        field_name="destination_country__country_code_iso3",
        lookup_expr="iexact")
    trade_bloc_name_pt = CharFilter(
        field_name="destination_country__trade_bloc__bloc_name_pt",
        lookup_expr="iexact")
    trade_bloc_name_en = CharFilter(
        field_name="destination_country__trade_bloc__bloc_name_en",
        lookup_expr="iexact")
    trade_bloc_name_es = CharFilter(
        field_name="destination_country__trade_bloc__bloc_name_es",
        lookup_expr="iexact")
    trade_bloc_code = CharFilter(
        field_name="destination_country__trade_bloc__bloc_code",
        lookup_expr="iexact")
    federative_unity_name = CharFilter(
        field_name="origin_fed_unit__uf_name", lookup_expr="iexact")
    federative_unity_code = CharFilter(
        field_name="origin_fed_unit__uf_code", lookup_expr="iexact")
    federative_unity_initials = CharFilter(
        field_name="origin_fed_unit__uf_initials", lookup_expr="iexact")
    transportation_name = CharFilter(
        field_name="transportation__transportation_name",
        lookup_expr="iexact")
    transportation_code = CharFilter(
        field_name="transportation__transportation_code",
        lookup_expr="iexact")
    ncm_code = CharFilter(
        field_name="ncm__ncm_code",
        lookup_expr="iexact")
    statistic_unit_code = CharFilter(
        field_name="ncm__statistic_unit_code",
        lookup_expr="iexact")
    ppe_code = CharFilter(
        field_name="ncm__ppe_code",
        lookup_expr="iexact")
    ppi_code = CharFilter(
        field_name="ncm__ppi_code",
        lookup_expr="iexact")
    aggregate_factor_code = CharFilter(
        field_name="ncm__aggregate_factor_code",
        lookup_expr="iexact")
    isic4_code = CharFilter(
        field_name="ncm__isic4_code",
        lookup_expr="iexact")
    exportation_subset = CharFilter(
        field_name="ncm__exportation_subset",
        lookup_expr="iexact")
    siit_code = CharFilter(
        field_name="ncm__siit_code",
        lookup_expr="iexact")
    cuci_item_code = CharFilter(
        field_name="ncm__cuci__item_code",
        lookup_expr="iexact")
    cuci_subitem_code = CharFilter(
        field_name="ncm__cuci__subitem_code",
        lookup_expr="iexact")
    cuci_position_code = CharFilter(
        field_name="ncm__cuci__position_code",
        lookup_expr="iexact")
    cuci_chapter_code = CharFilter(
        field_name="ncm__cuci__chapter_code",
        lookup_expr="iexact")
    cuci_section_code = CharFilter(
        field_name="ncm__cuci__section_code",
        lookup_expr="iexact")
    cgce_level1_code = CharFilter(
        field_name="ncm__cgce__level1_code",
        lookup_expr="iexact"
    )
    cgce_level2_code = CharFilter(
        field_name="ncm__cgce__level2_code",
        lookup_expr="iexact"
    )
    cgce_level3_code = CharFilter(
        field_name="ncm__cgce__level3_code",
        lookup_expr="iexact"
    )
    sh_chapter_code = CharFilter(
        field_name="ncm__sh__chapter_code",
        lookup_expr="iexact"
    )
    sh_position_code = CharFilter(
        field_name="ncm__sh__position_code",
        lookup_expr="iexact"
    )
    sh_subposition_code = CharFilter(
        field_name="ncm__sh__subposition_code",
        lookup_expr="iexact"
    )
    sh_section_code = CharFilter(
        field_name="ncm__sh__section_code",
        lookup_expr="iexact"
    )

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
            'ncm_code': ['iexact'],
            'ncm_name_pt': ['icontains'],
            'ncm_name_en': ['icontains'],
            'ncm_name_es': ['icontains'],
            'statistic_unit_code': ['iexact'],
            'ppe_code': ['iexact'],
            'ppi_code': ['iexact'],
            'aggregate_factor_code': ['iexact'],
            'cuci': [],
            'cgce': [],
            'sh': [],
            'isic4_code': ['iexact'],
            'exportation_subset': ['iexact'],
            'siit_code': ['iexact']
        }
        interfaces = {graphene.Node, }


class CUCIType(DjangoObjectType):
    class Meta:
        model = CUCI
        filter_fields = {
            'item_code': ['iexact'],
            'item_name_pt': ['icontains'],
            'item_name_en': ['icontains'],
            'item_name_es': ['icontains'],
            'subitem_code': ['iexact'],
            'subitem_name_pt': ['icontains'],
            'subitem_name_en': ['icontains'],
            'subitem_name_es': ['icontains'],
            'position_code': ['iexact'],
            'position_name_pt': ['icontains'],
            'position_name_en': ['icontains'],
            'position_name_es': ['icontains'],
            'chapter_code': ['iexact'],
            'chapter_name_pt': ['icontains'],
            'chapter_name_en': ['icontains'],
            'chapter_name_es': ['icontains'],
            'section_code': ['iexact'],
            'section_name_pt': ['icontains'],
            'section_name_en': ['icontains'],
            'section_name_es': ['icontains']
        }
        interfaces = {graphene.Node, }


class CGCEType(DjangoObjectType):
    class Meta:
        model = CGCE
        filter_fields = {
            'level1_code': ['iexact'],
            'level1_name_pt': ['icontains'],
            'level1_name_en': ['icontains'],
            'level1_name_es': ['icontains'],
            'level2_code': ['iexact'],
            'level2_name_pt': ['icontains'],
            'level2_name_en': ['icontains'],
            'level2_name_es': ['icontains'],
            'level3_code': ['iexact'],
            'level3_name_pt': ['icontains'],
            'level3_name_en': ['icontains'],
            'level3_name_es': ['icontains']
        }
        interfaces = {graphene.Node, }


class SHType(DjangoObjectType):
    class Meta:
        model = SH
        filter_fields = {
            'chapter_code': ['iexact'],
            'chapter_name_pt': ['icontains'],
            'chapter_name_en': ['icontains'],
            'chapter_name_es': ['icontains'],
            'position_code': ['iexact'],
            'position_name_pt': ['icontains'],
            'position_name_en': ['icontains'],
            'position_name_es': ['icontains'],
            'subposition_code': ['iexact'],
            'subposition_name_pt': ['icontains'],
            'subposition_name_en': ['icontains'],
            'subposition_name_es': ['icontains'],
            'section_code': ['iexact'],
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
            'bloc_code': ['iexact']
        }
        interfaces = {graphene.Node, }


class CountryType(DjangoObjectType):
    class Meta:
        model = Country
        filter_fields = {
            'country_name_pt': ['icontains'],
            'country_name_en': ['icontains'],
            'country_name_es': ['icontains'],
            'country_code_iso3': ['iexact']
        }
        interfaces = {graphene.Node, }


class FederativeUnitType(DjangoObjectType):
    class Meta:
        model = FederativeUnit
        filter_fields = {
            'uf_code': ['iexact'],
            'uf_name': ['iexact'],
            'uf_initials': ['iexact']
        }
        interfaces = {graphene.Node, }


class TransportationType(DjangoObjectType):
    class Meta:
        model = Transportation
        filter_fields = {
            'transportation_name': ['icontains'],
            'transportation_code': ['iexact']
        }
        interfaces = {graphene.Node, }


class UrfType(DjangoObjectType):
    class Meta:
        model = Urf
        filter_fields = {
            'urf_code': ['iexact'],
            'urf_name': ['iexact'],
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
