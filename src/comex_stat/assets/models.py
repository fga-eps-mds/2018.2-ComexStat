from django.db import models
from datetime import datetime

class AssetFacts(models.Model):
    date = models.DateField(default=datetime.now)
    origin = models.CharField(max_length=100)
    destination = models.CharField(max_length=100)
    class Meta:
        abstract = True


class AssetImportFacts(AssetFacts):
    pass


class AssetExportFacts(AssetFacts):
    pass
