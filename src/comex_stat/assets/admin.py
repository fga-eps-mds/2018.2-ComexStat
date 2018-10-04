from django.contrib import admin
from comex_stat.assets.models import (AssetImportFacts, AssetExportFacts,
                                      TradeBlocs, Country, FederativeUnit,
                                      Transportation, Urf, NCM, CUCI, CGCE, SH)

admin.site.register(AssetExportFacts)
admin.site.register(AssetImportFacts)
admin.site.register(TradeBlocs)
admin.site.register(Country)
admin.site.register(FederativeUnit)
admin.site.register(Transportation)
admin.site.register(Urf)
admin.site.register(NCM)
admin.site.register(CUCI)
admin.site.register(CGCE)
admin.site.register(SH)
