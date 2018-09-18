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


class AssetFacts(models.Model):
    date = models.DateField(default=datetime.now)
    name = models.CharField(max_length=100)
    ncm = models.ForeignKey(NCM, on_delete=models.CASCADE)
    port = models.CharField(max_length=100)
    port_code = models.CharField(max_length=100)
    transportation = models.CharField(max_length=100)
    registries = models.BigIntegerField()
    net_kilogram = models.FloatField()
    fob_value = models.FloatField()

    class Meta:
        abstract = True


class AssetImportFacts(AssetFacts):
    destination_fed_unit = models.CharField(max_length=100)
    origin_country = models.CharField(max_length=100)
    pass


class AssetExportFacts(AssetFacts):
    origin_fed_unit = models.CharField(max_length=100)
    destination_country = models.CharField(max_length=100)
    pass
