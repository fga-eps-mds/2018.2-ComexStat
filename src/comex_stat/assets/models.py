from django.db import models
from datetime import datetime


class NCM(models.Model):
    ncm = models.CharField(max_length=250)
    unid = models.CharField(max_length=100)
    ppe = models.CharField(max_length=100)
    ppi = models.CharField(max_length=100)
    fat_agreg = models.CharField(max_length=100)
    isic4 = models.CharField(max_length=100)
    exp_subset = models.CharField(max_length=100)
    ncm_por = models.CharField(max_length=100)
    ncm_en = models.CharField(max_length=100)
    ncm_es = models.CharField(max_length=100)
    siit = models.CharField(max_length=100)


class TradeBlocs(models.Model):
    bloc_name_pt = models.CharField(max_length=100)
    bloc_name_en = models.CharField(max_length=100)
    bloc_name_sp = models.CharField(max_length=100)
    bloc_code = models.CharField(max_length=100)


class Country(models.Model):
    country_name_pt = models.CharField(max_length=100)
    country_name_en = models.CharField(max_length=100)
    country_name_sp = models.CharField(max_length=100)
    country_code_iso3 = models.CharField(max_length=100)
    trade_bloc = models.ForeignKey(TradeBlocs, on_delete=models.CASCADE)


class FedUnit(models.Model):
    uf_name = models.CharField(max_length=100)
    uf_code = models.CharField(max_length=100)
    uf_initials = models.CharField(max_length=100)


class Transportation(models.Model):
    transportation_name = models.CharField(max_length=100)
    transportation_code = models.CharField(max_length=100)


class Urf(models.Model):
    urf_name = models.CharField(max_length=100)
    urf_code = models.CharField(max_length=100)


class AssetFacts(models.Model):
    date = models.DateField(default=datetime.now)
    name = models.CharField(max_length=100)
    ncm = models.ForeignKey(NCM, on_delete=models.CASCADE)
    urf = models.ForeignKey(Urf, on_delete=models.CASCADE, null=True)
    transportation = models.ForeignKey(
        Transportation, on_delete=models.CASCADE)
    registries = models.BigIntegerField()
    net_kilogram = models.FloatField()
    fob_value = models.FloatField()

    class Meta:
        abstract = True


class AssetImportFacts(AssetFacts):
    destination_fed_unit = models.ForeignKey(FedUnit, on_delete=models.CASCADE)
    origin_country = models.ForeignKey(Country, on_delete=models.CASCADE)


class AssetExportFacts(AssetFacts):
    origin_fed_unit = models.ForeignKey(FedUnit, on_delete=models.CASCADE)
    destination_country = models.ForeignKey(Country, on_delete=models.CASCADE)
