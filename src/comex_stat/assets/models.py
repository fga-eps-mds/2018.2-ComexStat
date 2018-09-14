from django.db import models
from datetime import datetime

class AssetFacts(models.Model):
    date = models.DateField(default=datetime.now)
    name = models.CharField(max_length=100)
    ncm = models.CharField(max_length=250)
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
