import graphene

from graphene_django.types import DjangoObjectType
from graphene_django.filter.fields import DjangoFilterConnectionField
from comex_stat.assets.models import (AssetImportFacts, AssetExportFacts,
                                      NCM, TradeBlocs, Country, FederativeUnit,
                                      Transportation, Urf)


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


class Query(object):
    all_import = DjangoFilterConnectionField(AssetImportFactsType)
    all_export = DjangoFilterConnectionField(AssetExportFactsType)
    all_ncm = graphene.List(NCMType)
    all_tradeBlocs = DjangoFilterConnectionField(TradeBlocsType)
    all_country = DjangoFilterConnectionField(CountryType)
    all_federativeUnit = DjangoFilterConnectionField(FederativeUnitType)
    all_transportation = DjangoFilterConnectionField(TransportationType)
    all_urf = DjangoFilterConnectionField(UrfType)

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
