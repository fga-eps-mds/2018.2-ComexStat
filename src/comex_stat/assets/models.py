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


class AssetExportFacts(AssetFacts):
    origin_fed_unit = models.CharField(max_length=100)
    destination_country = models.CharField(max_length=100)
