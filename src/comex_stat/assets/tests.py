from django.test import TestCase

from comex_stat.assets.models import (AssetImportFacts, AssetExportFacts,
                                      TradeBlocs, Country, FederativeUnit,
                                      Transportation, Urf)


class AssetImportTest(TestCase):

    entry = AssetImportFacts()

    def test_date_representation(self):
        self.assertEquals()
