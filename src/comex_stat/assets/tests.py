import graphene
# import json
from django.test import TestCase
from django.db import IntegrityError
from comex_stat.assets.schema import Query
from comex_stat.assets.models import (AssetImportFacts, AssetExportFacts,
                                      TradeBlocs, Country, FederativeUnit,
                                      Transportation, Urf, NCM, CUCI, CGCE, SH)


class AssetExportFactsTestModel(TestCase):

    def setUp(self):
        """
            This method will run before each test
        """

        self.tradeBlocs = TradeBlocs.objects.create(
            name_portuguese="portuguese",
            name_english="english",
            name_spanish="spanish",
            code="190"
        )

        self.country = Country.objects.create(
            name_portuguese="Nome",
            name_english="Name",
            name_spanish="Nombre",
            code_iso3="190",
            trade_bloc=self.tradeBlocs
        )

        self.federativeUnit = FederativeUnit.objects.create(
            name="Name",
            code="9090",
            initials="SP"
        )

        self.urf = Urf.objects.create(
            name="name",
            code="code"
        )

        self.transportation = Transportation.objects.create(
            name="Name",
            code="code"
        )

        self.sh = SH.objects.create(
            chapter_code="5555",
            chapter_name_pt="abcd",
            chapter_name_en="efdg",
            chapter_name_es="ghij",
            position_code="6666",
            position_name_pt="klmn",
            position_name_en="nopq",
            position_name_es="rstu",
            subposition_code="7777",
            subposition_name_pt="vwyz",
            subposition_name_en="asdf",
            subposition_name_es="ghjk",
            section_code="8888",
            section_name_pt="ideia",
            section_name_en="test",
            section_name_es="teste"
        )

        self.cgce = CGCE.objects.create(
            level1_code="2222",
            level1_name_pt="texto",
            level1_name_en="text",
            level1_name_es="texto",
            level2_code="3333",
            level2_name_pt="algo",
            level2_name_en="something",
            level2_name_es="algo",
            level3_code="4444",
            level3_name_pt="teste",
            level3_name_en="test",
            level3_name_es="teste"
        )

        self.cuci = CUCI.objects.create(
            item_code="1234",
            item_name_pt="Nome",
            item_name_en="Name",
            item_name_es="Nombre",
            subitem_code="5678",
            subitem_name_pt="nome",
            subitem_name_en="name",
            subitem_name_es="nombre",
            position_code="0000",
            position_name_pt="posicao",
            position_name_en="position",
            position_name_es="posicion",
            chapter_code="1111",
            chapter_name_pt="capitulo",
            chapter_name_en="chapter",
            chapter_name_es="capitulo",
            section_code="2222",
            section_name_pt="secao",
            section_name_en="section",
            section_name_es="seccion"
        )

        self.ncm = NCM.objects.create(
            ncm_code="84099190",
            statistic_unit_code="10",
            ppe_code="3193",
            ppi_code="3172",
            aggregate_factor_code="03",
            isic4_code="29",
            exportation_subset="1005",
            ncm_name_pt="Outras partes para motores de explosao",
            ncm_name_en="Other parts for internal combustion engines",
            ncm_name_es="Otras partes para motores de explosion",
            siit_code="2000",
            cuci=self.cuci,
            cgce=self.cgce,
            sh=self.sh
        )

        self.AssetExportFacts = AssetExportFacts.objects.create(
            date="2018-09-21",
            name="Outras partes para motores de explosao",
            ncm=self.ncm,
            urf=self.urf,
            transportation=self.transportation,
            registries=1,
            net_kilogram=1,
            fob_value=191,
            origin_fed_unit=self.federativeUnit,
            destination_country=self.country
        )

    def test_instaced(self):
        """
            This will test if the object are being instaced
        """
        self.assertIsNotNone(self.AssetExportFacts)

    def test_instaced_country(self):
        """
            This will test if the object are being instaced
        """
        self.assertIsNotNone(self.country)

    def test_instaced_trade_blocks(self):
        """
            This will test if the object are being instaced
        """
        self.assertIsNotNone(self.tradeBlocs)

    def test_instaced_federative_unit(self):
        """
            This will test if the object are being instaced
        """
        self.assertIsNotNone(self.federativeUnit)

    def test_instaced_transportation(self):
        """
            This will test if the object are being instaced
        """
        self.assertIsNotNone(self.transportation)

    def test_instaced_urf(self):
        """
            This will test if the object are being instaced
        """
        self.assertIsNotNone(self.urf)

    def test_facts_relations(self):
        """
            This method will test if the export relations are beeing linked
            as they should
        """

        self.assertIs(self.ncm, self.AssetExportFacts.ncm)
        self.assertIs(self.urf, self.AssetExportFacts.urf)
        self.assertIs(self.transportation,
                      self.AssetExportFacts.transportation)
        self.assertIs(self.federativeUnit, self.
                      AssetExportFacts.origin_fed_unit)
        self.assertIs(self.country, self.
                      AssetExportFacts.destination_country)

    def test_cascade_delete_ncm(self):
        """
          This will test the deletion cascade
        """
        self.ncm.delete()

        with self.assertRaises(AssetExportFacts.DoesNotExist):
            AssetExportFacts.objects.get()

    def test_cascade_delete_urf(self):
        """
          This will test the deletion cascade
        """
        self.urf.delete()

        with self.assertRaises(AssetExportFacts.DoesNotExist):
            AssetExportFacts.objects.get()

    def test_cascade_delete_transportation(self):
        """
          This will test the deletion cascade
        """
        self.transportation.delete()

        with self.assertRaises(AssetExportFacts.DoesNotExist):
            AssetExportFacts.objects.get()

    def test_cascade_delete_federative_unit(self):
        """
          This will test the deletion cascade
        """
        self.federativeUnit.delete()

        with self.assertRaises(AssetExportFacts.DoesNotExist):
            AssetExportFacts.objects.get()

    def test_cascade_delete_country(self):
        """
          This will test the deletion cascade
        """
        self.country.delete()

        with self.assertRaises(AssetExportFacts.DoesNotExist):
            AssetExportFacts.objects.get()

    def test_missing_ncm(self):
        """
          This will test if it's possible to create the object without the
          foreign key
        """
        with self.assertRaises(IntegrityError):
            self.AssetExportFacts = AssetExportFacts.objects.create(
                date="2018-09-21",
                name="Outras partes para motores de explosao",
                urf=self.urf,
                transportation=self.transportation,
                registries=1,
                net_kilogram=1,
                fob_value=191,
                origin_fed_unit=self.federativeUnit,
                destination_country=self.country
            )

    def test_missing_transportation(self):
        """
          This will test if it's possible to create the object without the
          foreign key
        """
        with self.assertRaises(IntegrityError):
            self.AssetExportFacts = AssetExportFacts.objects.create(
                date="2018-09-21",
                name="Outras partes para motores de explosao",
                ncm=self.ncm,
                urf=self.urf,
                registries=1,
                net_kilogram=1,
                fob_value=191,
                origin_fed_unit=self.federativeUnit,
                destination_country=self.country
            )

    def test_missing_federative_unit(self):
        """
          This will test if it's possible to create the object without the
          foreign key
        """
        with self.assertRaises(IntegrityError):
            self.AssetExportFacts = AssetExportFacts.objects.create(
                date="2018-09-21",
                name="Outras partes para motores de explosao",
                ncm=self.ncm,
                urf=self.urf,
                transportation=self.transportation,
                registries=1,
                net_kilogram=1,
                fob_value=191,
                destination_country=self.country
            )

    def test_missing_country(self):
        """
          This will test if it's possible to create the object without the
          foreign key
        """
        with self.assertRaises(IntegrityError):
            self.AssetExportFacts = AssetExportFacts.objects.create(
                date="2018-09-21",
                name="Outras partes para motores de explosao",
                ncm=self.ncm,
                urf=self.urf,
                transportation=self.transportation,
                registries=1,
                net_kilogram=1,
                fob_value=191,
                origin_fed_unit=self.federativeUnit,
            )


class AssetImportFactsTestModel(TestCase):

    def setUp(self):
        """
            This method will run before each test
        """

        self.tradeBlocs = TradeBlocs.objects.create(
            name_portuguese="portuguese",
            name_english="english",
            name_spanish="spanish",
            code="190"
        )

        self.country = Country.objects.create(
            name_portuguese="Nome",
            name_english="Name",
            name_spanish="Nombre",
            code_iso3="190",
            trade_bloc=self.tradeBlocs
        )

        self.federativeUnit = FederativeUnit.objects.create(
            name="Name",
            code="9090",
            initials="SP"
        )

        self.urf = Urf.objects.create(
            name="name",
            code="code"
        )

        self.transportation = Transportation.objects.create(
            name="Name",
            code="code"
        )

        self.sh = SH.objects.create(
            chapter_code="5555",
            chapter_name_pt="abcd",
            chapter_name_en="efdg",
            chapter_name_es="ghij",
            position_code="6666",
            position_name_pt="klmn",
            position_name_en="nopq",
            position_name_es="rstu",
            subposition_code="7777",
            subposition_name_pt="vwyz",
            subposition_name_en="asdf",
            subposition_name_es="ghjk",
            section_code="8888",
            section_name_pt="ideia",
            section_name_en="test",
            section_name_es="teste"
        )

        self.cgce = CGCE.objects.create(
            level1_code="2222",
            level1_name_pt="texto",
            level1_name_en="text",
            level1_name_es="texto",
            level2_code="3333",
            level2_name_pt="algo",
            level2_name_en="something",
            level2_name_es="algo",
            level3_code="4444",
            level3_name_pt="teste",
            level3_name_en="test",
            level3_name_es="teste"
        )

        self.cuci = CUCI.objects.create(
            item_code="1234",
            item_name_pt="Nome",
            item_name_en="Name",
            item_name_es="Nombre",
            subitem_code="5678",
            subitem_name_pt="nome",
            subitem_name_en="name",
            subitem_name_es="nombre",
            position_code="0000",
            position_name_pt="posicao",
            position_name_en="position",
            position_name_es="posicion",
            chapter_code="1111",
            chapter_name_pt="capitulo",
            chapter_name_en="chapter",
            chapter_name_es="capitulo",
            section_code="2222",
            section_name_pt="secao",
            section_name_en="section",
            section_name_es="seccion"
        )

        self.ncm = NCM.objects.create(
            ncm_code="84099190",
            statistic_unit_code="10",
            ppe_code="3193",
            ppi_code="3172",
            aggregate_factor_code="03",
            isic4_code="29",
            exportation_subset="1005",
            ncm_name_pt="Outras partes para motores de explosao",
            ncm_name_en="Other parts for internal combustion engines",
            ncm_name_es="Otras partes para motores de explosion",
            siit_code="2000",
            cuci=self.cuci,
            cgce=self.cgce,
            sh=self.sh
        )

        self.AssetImportFacts = AssetImportFacts.objects.create(
            date="2018-09-22",
            name="Texto",
            ncm=self.ncm,
            urf=self.urf,
            transportation=self.transportation,
            registries=1,
            net_kilogram=1,
            fob_value=191,
            destination_fed_unit=self.federativeUnit,
            origin_country=self.country
        )

    def test_instaced(self):
        """
            This will test if the object are being instaced
        """
        self.assertIsNotNone(self.AssetImportFacts)

    def test_instaced_country(self):
        """
            This will test if the object are being instaced
        """
        self.assertIsNotNone(self.country)

    def test_instaced_trade_blocks(self):
        """
            This will test if the object are being instaced
        """
        self.assertIsNotNone(self.tradeBlocs)

    def test_instaced_federative_unit(self):
        """
            This will test if the object are being instaced
        """
        self.assertIsNotNone(self.federativeUnit)

    def test_instaced_transportation(self):
        """
            This will test if the object are being instaced
        """
        self.assertIsNotNone(self.transportation)

    def test_instaced_urf(self):
        """
            This will test if the object are being instaced
        """
        self.assertIsNotNone(self.urf)

    def test_facts_relations(self):
        """
            This method will test if the import relations are beeing linked
            as they should
        """

        self.assertIs(self.ncm, self.AssetImportFacts.ncm)
        self.assertIs(self.urf, self.AssetImportFacts.urf)
        self.assertIs(self.transportation,
                      self.AssetImportFacts.transportation)
        self.assertIs(self.federativeUnit, self.
                      AssetImportFacts.destination_fed_unit)
        self.assertIs(self.country, self.
                      AssetImportFacts.origin_country)

    def test_cascade_delete_ncm(self):
        """
          This will test the deletion cascade
        """
        self.ncm.delete()

        with self.assertRaises(AssetImportFacts.DoesNotExist):
            AssetImportFacts.objects.get()

    def test_cascade_delete_urf(self):
        """
          This will test the deletion cascade
        """
        self.urf.delete()

        with self.assertRaises(AssetImportFacts.DoesNotExist):
            AssetImportFacts.objects.get()

    def test_cascade_delete_transportation(self):
        """
          This will test the deletion cascade
        """
        self.transportation.delete()

        with self.assertRaises(AssetImportFacts.DoesNotExist):
            AssetImportFacts.objects.get()

    def test_cascade_delete_federative_unit(self):
        """
          This will test the deletion cascade
        """
        self.federativeUnit.delete()

        with self.assertRaises(AssetImportFacts.DoesNotExist):
            AssetImportFacts.objects.get()

    def test_cascade_delete_country(self):
        """
          This will test the deletion cascade
        """
        self.country.delete()

        with self.assertRaises(AssetImportFacts.DoesNotExist):
            AssetImportFacts.objects.get()

    def test_missing_ncm(self):
        """
          This will test if it's possible to create the object without the
          foreign key
        """
        with self.assertRaises(IntegrityError):
            self.AssetImportFacts = AssetImportFacts.objects.create(
                date="2018-09-21",
                name="Outras partes para motores de explosao",
                urf=self.urf,
                transportation=self.transportation,
                registries=1,
                net_kilogram=1,
                fob_value=191,
                destination_fed_unit=self.federativeUnit,
                origin_country=self.country
            )

    def test_missing_transportation(self):
        """
          This will test if it's possible to create the object without the
          foreign key
        """
        with self.assertRaises(IntegrityError):
            self.AssetImportFacts = AssetImportFacts.objects.create(
                date="2018-09-21",
                name="Outras partes para motores de explosao",
                ncm=self.ncm,
                urf=self.urf,
                registries=1,
                net_kilogram=1,
                fob_value=191,
                destination_fed_unit=self.federativeUnit,
                origin_country=self.country
            )

    def test_missing_federative_unit(self):
        """
          This will test if it's possible to create the object without the
          foreign key
        """
        with self.assertRaises(IntegrityError):
            self.AssetImportFacts = AssetImportFacts.objects.create(
                date="2018-09-21",
                name="Outras partes para motores de explosao",
                ncm=self.ncm,
                urf=self.urf,
                transportation=self.transportation,
                registries=1,
                net_kilogram=1,
                fob_value=191,
                origin_country=self.country
            )

    def test_missing_country(self):
        """
          This will test if it's possible to create the object without the
          foreign key
        """
        with self.assertRaises(IntegrityError):
            self.AssetImportFacts = AssetImportFacts.objects.create(
                date="2018-09-21",
                name="Outras partes para motores de explosao",
                ncm=self.ncm,
                urf=self.urf,
                transportation=self.transportation,
                registries=1,
                net_kilogram=1,
                fob_value=191,
                destination_fed_unit=self.federativeUnit,
            )


class QueryTest(TestCase):

    def setUp(self):
        """
            This method will run before each test
        """

        self.tradeBlocs = TradeBlocs.objects.create(
            name_portuguese="portuguese",
            name_english="english",
            name_spanish="spanish",
            code="190"
        )

        self.country = Country.objects.create(
            name_portuguese="Nome",
            name_english="Name",
            name_spanish="Nombre",
            code_iso3="190",
            trade_bloc=self.tradeBlocs
        )

        self.federativeUnit = FederativeUnit.objects.create(
            name="Name",
            code="9090",
            initials="SP"
        )

        self.urf = Urf.objects.create(
            name="name",
            code="code"
        )

        self.transportation = Transportation.objects.create(
            name="Name",
            code="code"
        )

        self.sh = SH.objects.create(
            chapter_code="5555",
            chapter_name_pt="abcd",
            chapter_name_en="efdg",
            chapter_name_es="ghij",
            position_code="6666",
            position_name_pt="klmn",
            position_name_en="nopq",
            position_name_es="rstu",
            subposition_code="7777",
            subposition_name_pt="vwyz",
            subposition_name_en="asdf",
            subposition_name_es="ghjk",
            section_code="8888",
            section_name_pt="ideia",
            section_name_en="test",
            section_name_es="teste"
        )

        self.cgce = CGCE.objects.create(
            level1_code="2222",
            level1_name_pt="texto",
            level1_name_en="text",
            level1_name_es="texto",
            level2_code="3333",
            level2_name_pt="algo",
            level2_name_en="something",
            level2_name_es="algo",
            level3_code="4444",
            level3_name_pt="teste",
            level3_name_en="test",
            level3_name_es="teste"
        )

        self.cuci = CUCI.objects.create(
            item_code="1234",
            item_name_pt="Nome",
            item_name_en="Name",
            item_name_es="Nombre",
            subitem_code="5678",
            subitem_name_pt="nome",
            subitem_name_en="name",
            subitem_name_es="nombre",
            position_code="0000",
            position_name_pt="posicao",
            position_name_en="position",
            position_name_es="posicion",
            chapter_code="1111",
            chapter_name_pt="capitulo",
            chapter_name_en="chapter",
            chapter_name_es="capitulo",
            section_code="2222",
            section_name_pt="secao",
            section_name_en="section",
            section_name_es="seccion"
        )

        self.ncm = NCM.objects.create(
            ncm_code="84099190",
            statistic_unit_code="10",
            ppe_code="3193",
            ppi_code="3172",
            aggregate_factor_code="03",
            isic4_code="29",
            exportation_subset="1005",
            ncm_name_pt="Outras partes para motores de explosao",
            ncm_name_en="Other parts for internal combustion engines",
            ncm_name_es="Otras partes para motores de explosion",
            siit_code="2000",
            cuci=self.cuci,
            cgce=self.cgce,
            sh=self.sh
        )

        self.AssetExportFacts = AssetExportFacts.objects.create(
            date="2018-09-21",
            name="Outras partes para motores de explosao",
            ncm=self.ncm,
            urf=self.urf,
            transportation=self.transportation,
            registries=1,
            net_kilogram=1,
            fob_value=191,
            origin_fed_unit=self.federativeUnit,
            destination_country=self.country
        )

        self.AssetImportFacts = AssetImportFacts.objects.create(
            date="2018-09-22",
            name="Texto",
            ncm=self.ncm,
            urf=self.urf,
            transportation=self.transportation,
            registries=1,
            net_kilogram=1,
            fob_value=191,
            destination_fed_unit=self.federativeUnit,
            origin_country=self.country
        )

    def test_query_asset_import(self):
        query = query = '''
          query {
            allImport{
              edges {
                node {
                  date
                  name
                  ncm {
                    ncmCode
                    statisticUnitCode
                    ppeCode
                    ppiCode
                    aggregateFactorCode
                    isic4Code
                    exportationSubset
                    ncmNamePt
                    ncmNameEn
                    ncmNameEs
                    siitCode
                    cuci {
                      itemCode
                      itemNamePt
                      itemNameEn
                      itemNameEs
                      subitemCode
                      subitemNamePt
                      subitemNameEn
                      subitemNameEs
                      positionCode
                      positionNamePt
                      positionNameEn
                      positionNameEs
                      chapterCode
                      chapterNamePt
                      chapterNameEn
                      chapterNameEs
                      sectionCode
                      sectionNamePt
                      sectionNameEn
                      sectionNameEs
                    }
                    cgce {
                      level1Code
                      level1NamePt
                      level1NameEn
                      level1NameEs
                      level2Code
                      level2NamePt
                      level2NameEn
                      level2NameEs
                      level3Code
                      level3NamePt
                      level3NameEn
                      level3NameEs
                    }
                    sh {
                      chapterCode
                      chapterNamePt
                      chapterNameEn
                      chapterNameEs
                      positionCode
                      positionNamePt
                      positionNameEn
                      positionNameEs
                      subpositionCode
                      subpositionNamePt
                      subpositionNameEn
                      subpositionNameEs
                      sectionCode
                      sectionNamePt
                      sectionNameEn
                      sectionNameEs
                    }
                  }
                  urf {
                    name
                    code
                  }
                  transportation {
                    name
                    code
                  }
                  registries
                  netKilogram
                  fobValue
                  destinationFedUnit {
                    name
                    code
                    initials
                  }
                  originCountry {
                    namePortuguese
                    nameEnglish
                    nameSpanish
                    codeIso3
                    tradeBloc {
                      namePortuguese
                      nameEnglish
                      nameSpanish
                      code
                    }
                  }
                }
              }
            }
          }
      '''

        expected = {"allImport": {
                "edges": [
                    {
                        "node": {
                            "date": "2018-09-22",
                            "name": "Texto",
                            "ncm": {
                                "ncmCode": "84099190",
                                "statisticUnitCode": "10",
                                "ppeCode": "3193",
                                "ppiCode": "3172",
                                "aggregateFactorCode": "03",
                                "isic4Code": "29",
                                "exportationSubset": "1005",
                                "ncmNamePt":
                                "Outras partes para motores de explosao",
                                "ncmNameEn":
                                "Other parts for internal combustion engines",
                                "ncmNameEs":
                                "Otras partes para motores de explosion",
                                "siitCode": "2000",
                                "cuci": {
                                    "itemCode": "1234",
                                    "itemNamePt": "Nome",
                                    "itemNameEn": "Name",
                                    "itemNameEs": "Nombre",
                                    "subitemCode": "5678",
                                    "subitemNamePt": "nome",
                                    "subitemNameEn": "name",
                                    "subitemNameEs": "nombre",
                                    "positionCode": "0000",
                                    "positionNamePt": "posicao",
                                    "positionNameEn": "position",
                                    "positionNameEs": "posicion",
                                    "chapterCode": "1111",
                                    "chapterNamePt": "capitulo",
                                    "chapterNameEn": "chapter",
                                    "chapterNameEs": "capitulo",
                                    "sectionCode": "2222",
                                    "sectionNamePt": "secao",
                                    "sectionNameEn": "section",
                                    "sectionNameEs": "seccion"
                                },
                                "cgce": {
                                    "level1Code": "2222",
                                    "level1NamePt": "texto",
                                    "level1NameEn": "text",
                                    "level1NameEs": "texto",
                                    "level2Code": "3333",
                                    "level2NamePt": "algo",
                                    "level2NameEn": "something",
                                    "level2NameEs": "algo",
                                    "level3Code": "4444",
                                    "level3NamePt": "teste",
                                    "level3NameEn": "test",
                                    "level3NameEs": "teste"
                                },
                                "sh": {
                                    "chapterCode": "5555",
                                    "chapterNamePt": "abcd",
                                    "chapterNameEn": "efdg",
                                    "chapterNameEs": "ghij",
                                    "positionCode": "6666",
                                    "positionNamePt": "klmn",
                                    "positionNameEn": "nopq",
                                    "positionNameEs": "rstu",
                                    "subpositionCode": "7777",
                                    "subpositionNamePt": "vwyz",
                                    "subpositionNameEn": "asdf",
                                    "subpositionNameEs": "ghjk",
                                    "sectionCode": "8888",
                                    "sectionNamePt": "ideia",
                                    "sectionNameEn": "test",
                                    "sectionNameEs": "teste"
                                }
                            },
                            "urf": {
                                "name": "name",
                                "code": "code"
                            },
                            "transportation": {
                                "name": "Name",
                                "code": "code"
                            },
                            "registries": 1,
                            "netKilogram": 1.0,
                            "fobValue": 191.0,
                            "destinationFedUnit": {
                                "name": "Name",
                                "code": "9090",
                                "initials": "SP"
                            },
                            "originCountry": {
                                "namePortuguese": "Nome",
                                "nameEnglish": "Name",
                                "nameSpanish": "Nombre",
                                "codeIso3": "190",
                                "tradeBloc": {
                                    "namePortuguese": "portuguese",
                                    "nameEnglish": "english",
                                    "nameSpanish": "spanish",
                                    "code": "190"
                                }
                            }
                        }
                    }
                ]
            }
         }

        schema = graphene.Schema(Query)
        result = schema.execute(query)
        self.assertEqual(expected, result.data)

    def test_query_asset_export(self):
        query = query = '''
            query {
              allExport {
                edges {
                  node {
                    date
                    name
                    ncm {
                      ncmCode
                      statisticUnitCode
                      ppeCode
                      ppiCode
                      aggregateFactorCode
                      isic4Code
                      exportationSubset
                      ncmNamePt
                      ncmNameEn
                      ncmNameEs
                      siitCode
                      cuci {
                        itemCode
                        itemNamePt
                        itemNameEn
                        itemNameEs
                        subitemCode
                        subitemNamePt
                        subitemNameEn
                        subitemNameEs
                        positionCode
                        positionNamePt
                        positionNameEn
                        positionNameEs
                        chapterCode
                        chapterNamePt
                        chapterNameEn
                        chapterNameEs
                        sectionCode
                        sectionNamePt
                        sectionNameEn
                        sectionNameEs
                      }
                      cgce {
                        level1Code
                        level1NamePt
                        level1NameEn
                        level1NameEs
                        level2Code
                        level2NamePt
                        level2NameEn
                        level2NameEs
                        level3Code
                        level3NamePt
                        level3NameEn
                        level3NameEs
                      }
                      sh {
                        chapterCode
                        chapterNamePt
                        chapterNameEn
                        chapterNameEs
                        positionCode
                        positionNamePt
                        positionNameEn
                        positionNameEs
                        subpositionCode
                        subpositionNamePt
                        subpositionNameEn
                        subpositionNameEs
                        sectionCode
                        sectionNamePt
                        sectionNameEn
                        sectionNameEs
                      }
                    }
                    urf {
                      name
                      code
                    }
                    transportation {
                      name
                      code
                    }
                    registries
                    netKilogram
                    fobValue
                    originFedUnit {
                      name
                      code
                      initials
                    }
                    destinationCountry {
                      namePortuguese
                      nameEnglish
                      nameSpanish
                      codeIso3
                      tradeBloc {
                        namePortuguese
                        nameEnglish
                        nameSpanish
                        code
                      }
                    }
                  }
                }
              }
            }
        '''

        expected = {"allExport": {
                "edges": [
                    {
                        "node": {
                            "date": "2018-09-21",
                            "name": "Outras partes para motores de explosao",
                            "ncm": {
                                "ncmCode": "84099190",
                                "statisticUnitCode": "10",
                                "ppeCode": "3193",
                                "ppiCode": "3172",
                                "aggregateFactorCode": "03",
                                "isic4Code": "29",
                                "exportationSubset": "1005",
                                "ncmNamePt":
                                "Outras partes para motores de explosao",
                                "ncmNameEn":
                                "Other parts for internal combustion engines",
                                "ncmNameEs":
                                "Otras partes para motores de explosion",
                                "siitCode": "2000",
                                "cuci": {
                                    "itemCode": "1234",
                                    "itemNamePt": "Nome",
                                    "itemNameEn": "Name",
                                    "itemNameEs": "Nombre",
                                    "subitemCode": "5678",
                                    "subitemNamePt": "nome",
                                    "subitemNameEn": "name",
                                    "subitemNameEs": "nombre",
                                    "positionCode": "0000",
                                    "positionNamePt": "posicao",
                                    "positionNameEn": "position",
                                    "positionNameEs": "posicion",
                                    "chapterCode": "1111",
                                    "chapterNamePt": "capitulo",
                                    "chapterNameEn": "chapter",
                                    "chapterNameEs": "capitulo",
                                    "sectionCode": "2222",
                                    "sectionNamePt": "secao",
                                    "sectionNameEn": "section",
                                    "sectionNameEs": "seccion"
                                },
                                "cgce": {
                                    "level1Code": "2222",
                                    "level1NamePt": "texto",
                                    "level1NameEn": "text",
                                    "level1NameEs": "texto",
                                    "level2Code": "3333",
                                    "level2NamePt": "algo",
                                    "level2NameEn": "something",
                                    "level2NameEs": "algo",
                                    "level3Code": "4444",
                                    "level3NamePt": "teste",
                                    "level3NameEn": "test",
                                    "level3NameEs": "teste"
                                },
                                "sh": {
                                    "chapterCode": "5555",
                                    "chapterNamePt": "abcd",
                                    "chapterNameEn": "efdg",
                                    "chapterNameEs": "ghij",
                                    "positionCode": "6666",
                                    "positionNamePt": "klmn",
                                    "positionNameEn": "nopq",
                                    "positionNameEs": "rstu",
                                    "subpositionCode": "7777",
                                    "subpositionNamePt": "vwyz",
                                    "subpositionNameEn": "asdf",
                                    "subpositionNameEs": "ghjk",
                                    "sectionCode": "8888",
                                    "sectionNamePt": "ideia",
                                    "sectionNameEn": "test",
                                    "sectionNameEs": "teste"
                                }
                            },
                            "urf": {
                                "name": "name",
                                "code": "code"
                            },
                            "transportation": {
                                "name": "Name",
                                "code": "code"
                            },
                            "registries": 1,
                            "netKilogram": 1.0,
                            "fobValue": 191.0,
                            "originFedUnit": {
                                "name": "Name",
                                "code": "9090",
                                "initials": "SP"
                            },
                            "destinationCountry": {
                                "namePortuguese": "Nome",
                                "nameEnglish": "Name",
                                "nameSpanish": "Nombre",
                                "codeIso3": "190",
                                "tradeBloc": {
                                    "namePortuguese": "portuguese",
                                    "nameEnglish": "english",
                                    "nameSpanish": "spanish",
                                    "code": "190"
                                }
                            }
                        }
                    }
                ]
            }
         }

        schema = graphene.Schema(Query)
        result = schema.execute(query)
        # print(json.dumps(result.data), ident=4) --> You should first copy the
        # result of this to get the expected output to compare
        self.assertEqual(expected, result.data)
