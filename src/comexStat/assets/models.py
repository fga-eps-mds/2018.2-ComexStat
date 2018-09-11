from django.db import models


class AssetFacts(models.Model):
    class Meta:
        abstract = True


class AssetImportFacts(AssetFacts):
    name = models.CharField(max_length=100)


class AssetExportFacts(AssetFacts):
    pass
