from django.db import models
from datetime import datetime



class SH(models.Model):
    '''
        SH stands for Sistema Harmónico
    '''
    chapter_code = models.CharField(max_length=2,blank=False)
    chapter_name_pt = models.CharField(max_length=250,blank=False)
    chapter_name_en = models.CharField(max_length=250,blank=False)
    chapter_name_es = models.CharField(max_length=250,blank=False)
    position_code = models.CharField(max_length=4,blank=False)
    position_name_pt = models.CharField(max_length=250,blank=False)
    position_name_en = models.CharField(max_length=250,blank=False)
    position_name_es = models.CharField(max_length=250,blank=False)
    subposition_code = models.CharField(max_length=6,blank=False)
    subposition_name_pt = models.CharField(max_length=250,blank=False)
    subposition_name_en = models.CharField(max_length=250,blank=False)
    subposition_name_es = models.CharField(max_length=250,blank=False)
    section_code = models.CharField(max_length=2,blank=False)
    section_name_pt = models.CharField(max_length=250,blank=False)
    section_name_en = models.CharField(max_length=250,blank=False)
    section_name_es = models.CharField(max_length=250,blank=False)


class CGCE(models.Model):
    '''
        CGCE stands for Classificação por Grandes Categorias Econômicas
    '''
    level1_code = models.CharField(max_length=1,blank=False)
    level1_name_pt = models.CharField(max_length=250,blank=False)
    level1_name_en = models.CharField(max_length=250,blank=False)
    level1_name_es = models.CharField(max_length=250,blank=False)
    level2_code = models.CharField(max_length=2,blank=False)
    level2_name_pt = models.CharField(max_length=250,blank=False)
    level2_name_en = models.CharField(max_length=250,blank=False)
    level2_name_es = models.CharField(max_length=250,blank=False)
    level3_code = models.CharField(max_length=3,blank=False)
    level3_name_pt = models.CharField(max_length=250,blank=False)
    level3_name_en = models.CharField(max_length=250,blank=False)
    level3_name_es = models.CharField(max_length=250,blank=False)


class CUCI(models.Model):
    '''
        CUCI stands for Classificação Uniforme do Comércio Internacional
    '''
    item_code = models.CharField(max_length=5,blank=False)
    item_name_pt = models.CharField(max_length=250,blank=False)
    item_name_en = models.CharField(max_length=250,blank=False)
    item_name_es = models.CharField(max_length=250,blank=False)
    subitem_code = models.CharField(max_length=4,blank=False)
    subitem_name_pt = models.CharField(max_length=250,blank=False)
    subitem_name_en = models.CharField(max_length=250,blank=False)
    subitem_name_es = models.CharField(max_length=250,blank=False)
    position_code = models.CharField(max_length=3,blank=False)
    position_name_pt = models.CharField(max_length=250,blank=False)
    position_name_en = models.CharField(max_length=250,blank=False)
    position_name_es = models.CharField(max_length=250,blank=False)
    chapter_code = models.CharField(max_length=2,blank=False)
    chapter_name_pt = models.CharField(max_length=250,blank=False)
    chapter_name_en = models.CharField(max_length=250,blank=False)
    chapter_name_es = models.CharField(max_length=250,blank=False)
    section_code = models.CharField(max_length=1,blank=False)
    section_name_pt = models.CharField(max_length=250,blank=False)
    section_name_en = models.CharField(max_length=250,blank=False)
    section_name_es = models.CharField(max_length=250,blank=False)


class NCM(models.Model):
    '''
        NCM stands for Nomenclatura Comum do Mercosul
    '''
    ncm_code = models.CharField(max_length=8,blank=False)
    ncm_name_pt = models.CharField(max_length=250,blank=False)
    ncm_name_en = models.CharField(max_length=250,blank=False)
    ncm_name_es = models.CharField(max_length=250,blank=False)
    statistic_unit_code = models.CharField(max_length=2,blank=False)
    ppe_code = models.CharField(max_length=4,blank=False,verbose_name="Pauta de Produtos Exportados")
    ppi_code = models.CharField(max_length=4,blank=False,verbose_name="Pauta de Produtos Importados")
    aggregate_factor_code = models.CharField(max_length=1,blank=False)
    cuci = models.ForeignKey(CUCI, on_delete=models.CASCADE,verbose_name="Classificação Uniforme do Comércio Internacional")
    cgce = models.ForeignKey(CGCE, on_delete=models.CASCADE,verbose_name="Classificação por Grandes Categorias Econômicas")
    sh = models.ForeignKey(SH, on_delete=models.CASCADE,verbose_name="Sistema Harmónico")
    isic4_code = models.CharField(max_length=2,blank=False,verbose_name="International Standard Industrial Classification (Revision 4)")
    exportation_subset = models.CharField(max_length=4,blank=False)
    siit_code = models.CharField(max_length=4,blank=False,verbose_name="Setores Industriais por Intensidade Tecnológica")


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
