from django.db import models
from django.core.validators import RegexValidator
from datetime import datetime
validate_only_numbers = RegexValidator(regex="^[0-9]+$",
                                       message="Somente números são permitidos"
                                       )


class SH(models.Model):
    '''
        SH stands for Sistema Harmónico
    '''

    chapter_code = models.CharField(max_length=2, blank=True,
                                    validators=[validate_only_numbers])
    chapter_name_pt = models.TextField(blank=True)
    chapter_name_en = models.TextField()
    chapter_name_es = models.TextField()
    position_code = models.CharField(max_length=4, blank=False,
                                     validators=[validate_only_numbers])
    position_name_pt = models.TextField()
    position_name_en = models.TextField()
    position_name_es = models.TextField()
    subposition_code = models.CharField(max_length=6, blank=False,
                                        validators=[validate_only_numbers])
    subposition_name_pt = models.TextField()
    subposition_name_en = models.TextField()
    subposition_name_es = models.TextField()
    section_code = models.CharField(max_length=6, blank=False,
                                    verbose_name="Section code from NCM")
    section_name_pt = models.TextField()
    section_name_en = models.TextField()
    section_name_es = models.TextField()


class CGCE(models.Model):
    '''
        CGCE stands for Classificação por Grandes Categorias Econômicas
    '''
    level1_code = models.CharField(max_length=1, blank=False,
                                   validators=[validate_only_numbers])
    level1_name_pt = models.CharField(max_length=250, blank=False)
    level1_name_en = models.CharField(max_length=250, blank=False)
    level1_name_es = models.CharField(max_length=250, blank=False)
    level2_code = models.CharField(max_length=2, blank=False,
                                   validators=[validate_only_numbers])
    level2_name_pt = models.CharField(max_length=250, blank=False)
    level2_name_en = models.CharField(max_length=250, blank=False)
    level2_name_es = models.CharField(max_length=250, blank=False)
    level3_code = models.CharField(max_length=3, blank=False,
                                   validators=[validate_only_numbers])
    level3_name_pt = models.CharField(max_length=250, blank=False)
    level3_name_en = models.CharField(max_length=250, blank=False)
    level3_name_es = models.CharField(max_length=250, blank=False)


class CUCI(models.Model):
    '''
        CUCI stands for Classificação Uniforme do Comércio Internacional
    '''
    item_code = models.CharField(max_length=5, blank=False,
                                 validators=[validate_only_numbers])
    item_name_pt = models.TextField(blank=False)
    item_name_en = models.TextField(blank=False)
    item_name_es = models.TextField(blank=False)
    subitem_code = models.CharField(max_length=4, blank=False,
                                    validators=[validate_only_numbers])
    subitem_name_pt = models.TextField(blank=False)
    subitem_name_en = models.TextField(blank=False)
    subitem_name_es = models.TextField(blank=False)
    position_code = models.CharField(max_length=3, blank=False,
                                     validators=[validate_only_numbers])
    position_name_pt = models.TextField(blank=False)
    position_name_en = models.TextField(blank=False)
    position_name_es = models.TextField(blank=False)
    chapter_code = models.CharField(max_length=2, blank=False,
                                    validators=[validate_only_numbers])
    chapter_name_pt = models.TextField(blank=False)
    chapter_name_en = models.TextField(blank=False)
    chapter_name_es = models.TextField(blank=False)
    section_code = models.CharField(max_length=1, blank=False,
                                    verbose_name="Section code from NCM")
    section_name_pt = models.TextField(blank=False)
    section_name_en = models.TextField(blank=False)
    section_name_es = models.TextField(blank=False)


class NCM(models.Model):
    """
        NCM stands for Nomenclatura Comum do Mercosul
    """
    ncm_code = models.CharField(max_length=8, blank=False,
                                validators=[validate_only_numbers])
    ncm_name_pt = models.CharField(max_length=250, blank=False)
    ncm_name_en = models.CharField(max_length=250, blank=False)
    ncm_name_es = models.CharField(max_length=250, blank=False)
    statistic_unit_code = models.CharField(max_length=2, blank=False,
                                           validators=[validate_only_numbers])
    ppe_code = models.CharField(max_length=4, blank=False,
                                verbose_name="Pauta de Produtos Exportados",
                                validators=[validate_only_numbers])
    ppi_code = models.CharField(max_length=4, blank=False,
                                verbose_name="Pauta de Produtos Importados",
                                validators=[validate_only_numbers])
    aggregate_factor_code = models.CharField(max_length=1, blank=False,
                                             validators=[validate_only_numbers]
                                             )
    cuci = models.ForeignKey(CUCI, on_delete=models.CASCADE,
                             verbose_name='''Classificação Uniforme do
                                             Comércio Internacional''')
    cgce = models.ForeignKey(CGCE, on_delete=models.CASCADE,
                             verbose_name='''Classificação por Grandes
                                             Categorias Econômicas''')
    sh = models.ForeignKey(SH, on_delete=models.CASCADE,
                           verbose_name="Sistema Harmónico")
    isic4_code = models.CharField(max_length=2, blank=False,
                                  verbose_name='''International Standard Industrial
                                               Classification (Revision 4)''',
                                  validators=[validate_only_numbers])
    exportation_subset = models.CharField(max_length=4, blank=False)
    siit_code = models.CharField(max_length=4, blank=False,
                                 verbose_name='''Setores Industriais por
                                              Intensidade Tecnológica code''',
                                 validators=[validate_only_numbers])


class TradeBlocs(models.Model):
    bloc_name_pt = models.CharField(max_length=100)
    bloc_name_en = models.CharField(max_length=100)
    bloc_name_es = models.CharField(max_length=100)
    bloc_code = models.CharField(max_length=10)


class Country(models.Model):
    country_name_pt = models.CharField(max_length=100)
    country_name_en = models.CharField(max_length=100)
    country_name_es = models.CharField(max_length=100)
    country_code_iso3 = models.CharField(max_length=3)
    trade_bloc = models.ForeignKey(TradeBlocs, on_delete=models.CASCADE)


class FederativeUnit(models.Model):
    uf_name = models.CharField(max_length=100)
    uf_code = models.CharField(max_length=100)
    uf_initials = models.CharField(max_length=6)


class Transportation(models.Model):
    transportation_name = models.CharField(max_length=100)
    transportation_code = models.CharField(max_length=100)


class Urf(models.Model):
    urf_name = models.CharField(max_length=100)
    urf_code = models.CharField(max_length=100)


class AssetFacts(models.Model):
    date = models.DateField(default=datetime.now)
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
