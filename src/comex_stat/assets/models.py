from django.db import models


class AssetFacts(models.Model):
    class Meta:
        abstract = True


class AssetImportFacts(AssetFacts):
    pass


class AssetExportFacts(AssetFacts):
    pass
