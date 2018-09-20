from django.db import models
from datetime import datetime


class SH(models.Model):
    sh2 = models.CharField(max_length=250)
    sh2_pt = models.CharField(max_length=250)
    sh2_en = models.CharField(max_length=250)
    sh2_es = models.CharField(max_length=250)
    sh4 = models.CharField(max_length=250)
    sh4_pt = models.CharField(max_length=250)
    sh4_en = models.CharField(max_length=250)
    sh4_es = models.CharField(max_length=250)
    sh6 = models.CharField(max_length=250)
    sh6_pt = models.CharField(max_length=250)
    sh6_en = models.CharField(max_length=250)
    sh6_es = models.CharField(max_length=250)
    ncm_secrom = models.CharField(max_length=250)
    sec_pt = models.CharField(max_length=250)
    sec_en = models.CharField(max_length=250)
    sec_es = models.CharField(max_length=250)


class CGCE(models.Model):
    cgce_n1 = models.CharField(max_length=250)
    cgce_n1_pt = models.CharField(max_length=250)
    cgce_n1_en = models.CharField(max_length=250)
    cgce_n1_es = models.CharField(max_length=250)
    cgce_n2 = models.CharField(max_length=250)
    cgce_n2_pt = models.CharField(max_length=250)
    cgce_n2_en = models.CharField(max_length=250)
    cgce_n2_es = models.CharField(max_length=250)
    cgce_n3 = models.CharField(max_length=250)
    cgce_n3_pt = models.CharField(max_length=250)
    cgce_n3_en = models.CharField(max_length=250)
    cgce_n3_es = models.CharField(max_length=250)


class CUCI(models.Model):
    cuci_item = models.CharField(max_length=250)
    cuci_item_pt = models.CharField(max_length=250)
    cuci_item_en = models.CharField(max_length=250)
    cuci_item_es = models.CharField(max_length=250)
    cuci_sub = models.CharField(max_length=250)
    cuci_sub_pt = models.CharField(max_length=250)
    cuci_sub_en = models.CharField(max_length=250)
    cuci_sub_es = models.CharField(max_length=250)
    cuci_pos = models.CharField(max_length=250)
    cuci_pos_pt = models.CharField(max_length=250)
    cuci_pos_en = models.CharField(max_length=250)
    cuci_pos_es = models.CharField(max_length=250)
    cuci_cap = models.CharField(max_length=250)
    cuci_cap_pt = models.CharField(max_length=250)
    cuci_cap_en = models.CharField(max_length=250)
    cuci_cap_es = models.CharField(max_length=250)
    cuci_sec = models.CharField(max_length=250)
    cuci_sec_pt = models.CharField(max_length=250)
    cuci_sec_en = models.CharField(max_length=250)
    cuci_sec_es = models.CharField(max_length=250)


class NCM(models.Model):
    ncm = models.CharField(max_length=250)
    unid = models.CharField(max_length=100)
    ppe = models.CharField(max_length=100)
    ppi = models.CharField(max_length=100)
    fat_agreg = models.CharField(max_length=100)
    cuci = models.ForeignKey(CUCI, on_delete=models.CASCADE)
    cgce = models.ForeignKey(CGCE, on_delete=models.CASCADE)
    sh = models.ForeignKey(SH, on_delete=models.CASCADE)
    isic4 = models.CharField(max_length=100)
    exp_subset = models.CharField(max_length=100)
    ncm_pt = models.CharField(max_length=100)
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
