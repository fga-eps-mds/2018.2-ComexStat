from django.db import models
from datetime import datetime


class SH(models.Model):
    chapter_code = models.CharField(max_length=250)
    chapter_name_pt = models.CharField(max_length=250)
    chapter_name_en = models.CharField(max_length=250)
    chapter_name_es = models.CharField(max_length=250)
    position_code = models.CharField(max_length=250)
    position_name_pt = models.CharField(max_length=250)
    position_name_en = models.CharField(max_length=250)
    position_name_es = models.CharField(max_length=250)
    subposition_code = models.CharField(max_length=250)
    subposition_name_pt = models.CharField(max_length=250)
    subposition_name_en = models.CharField(max_length=250)
    subposition_name_es = models.CharField(max_length=250)
    section_code = models.CharField(max_length=250)
    section_name_pt = models.CharField(max_length=250)
    section_name_en = models.CharField(max_length=250)
    section_name_es = models.CharField(max_length=250)


class CGCE(models.Model):
    level1_code = models.CharField(max_length=250)
    level1_name_pt = models.CharField(max_length=250)
    level1_name_en = models.CharField(max_length=250)
    level1_name_es = models.CharField(max_length=250)
    level2_code = models.CharField(max_length=250)
    level2_name_pt = models.CharField(max_length=250)
    level2_name_en = models.CharField(max_length=250)
    level2_name_es = models.CharField(max_length=250)
    level3_code = models.CharField(max_length=250)
    level3_name_pt = models.CharField(max_length=250)
    level3_name_en = models.CharField(max_length=250)
    level3_name_es = models.CharField(max_length=250)


class CUCI(models.Model):
    item_code = models.CharField(max_length=250)
    item_name_pt = models.CharField(max_length=250)
    item_name_en = models.CharField(max_length=250)
    item_name_es = models.CharField(max_length=250)
    subitem_code = models.CharField(max_length=250)
    subitem_name_pt = models.CharField(max_length=250)
    subitem_name_en = models.CharField(max_length=250)
    subitem_name_es = models.CharField(max_length=250)
    position_code = models.CharField(max_length=250)
    position_name_pt = models.CharField(max_length=250)
    position_name_en = models.CharField(max_length=250)
    position_name_es = models.CharField(max_length=250)
    chapter_code = models.CharField(max_length=250)
    chapter_name_pt = models.CharField(max_length=250)
    chapter_name_en = models.CharField(max_length=250)
    chapter_name_es = models.CharField(max_length=250)
    section_code = models.CharField(max_length=250)  # Section from NCM
    section_name_pt = models.CharField(max_length=250)
    section_name_en = models.CharField(max_length=250)
    section_name_es = models.CharField(max_length=250)


class NCM(models.Model):
    ncm_code = models.CharField(max_length=250)
    ncm_name_pt = models.CharField(max_length=100)
    ncm_name_en = models.CharField(max_length=100)
    ncm_name_es = models.CharField(max_length=100)
    statistic_unit_code = models.CharField(max_length=100)
    ppe_code = models.CharField(max_length=100)
    ppi_code = models.CharField(max_length=100)
    aggregate_factor_code = models.CharField(max_length=100)
    cuci = models.ForeignKey(CUCI, on_delete=models.CASCADE)
    cgce = models.ForeignKey(CGCE, on_delete=models.CASCADE)
    sh = models.ForeignKey(SH, on_delete=models.CASCADE)
    isic4_code = models.CharField(max_length=100)
    exportation_subset = models.CharField(max_length=100)
    siit_code = models.CharField(max_length=100)


class TradeBlocs(models.Model):
    name_portuguese = models.CharField(max_length=100)
    name_english = models.CharField(max_length=100)
    name_spanish = models.CharField(max_length=100)
    code = models.CharField(max_length=10)


class Country(models.Model):
    name_portuguese = models.CharField(max_length=100)
    name_english = models.CharField(max_length=100)
    name_spanish = models.CharField(max_length=100)
    code_iso3 = models.CharField(max_length=3)
    trade_bloc = models.ForeignKey(TradeBlocs, on_delete=models.CASCADE)


class FederativeUnit(models.Model):
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=100)
    initials = models.CharField(max_length=6)


class Transportation(models.Model):
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=100)


class Urf(models.Model):
    # URF = "Federative Regional Unit", or "Unidade regional federativa" in pt
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=100)


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
    destination_fed_unit = models.ForeignKey(
        FederativeUnit, on_delete=models.CASCADE)
    origin_country = models.ForeignKey(Country, on_delete=models.CASCADE)


class AssetExportFacts(AssetFacts):
    origin_fed_unit = models.ForeignKey(
        FederativeUnit, on_delete=models.CASCADE)
    destination_country = models.ForeignKey(Country, on_delete=models.CASCADE)
