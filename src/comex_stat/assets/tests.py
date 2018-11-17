import graphene
from django.test import TestCase
from django.db import IntegrityError
from comex_stat.assets.schema import Query
from comex_stat.assets.models import (AssetImportFacts, AssetExportFacts,
                                      TradeBlocs, Country, FederativeUnit,
                                      Transportation, Urf, NCM, CUCI, CGCE, SH)
from django.core.exceptions import ValidationError
from collections import OrderedDict


class SHTests(TestCase):
    def create_sh(self, chapter_code, position_code, subposition_code):
        return SH.objects.create(chapter_code=chapter_code,
                                 position_code=position_code,
                                 subposition_code=subposition_code)

    def test_code_fields_do_not_accept_letters(self):
        """
            Test if a validation error occurs when a field that store a code
            tries to be saved with a letter or special char
        """
        sh = self.create_sh(chapter_code="#", position_code="4%3",
                            subposition_code="1-+=3")
        with self.assertRaises(ValidationError) as cm:
            sh.full_clean()

        self.assertTrue('chapter_code' in cm.exception.message_dict and
                        "Somente números são permitidos" in
                        cm.exception.message_dict['chapter_code'])
        self.assertTrue('position_code' in cm.exception.message_dict and
                        "Somente números são permitidos" in
                        cm.exception.message_dict['position_code'])
        self.assertTrue('subposition_code' in cm.exception.message_dict and
                        "Somente números são permitidos" in
                        cm.exception.message_dict['subposition_code'])


class CGCETests(TestCase):
    def create_cgce(self, level1_code, level2_code, level3_code):
        return CGCE.objects.create(level1_code=level1_code,
                                   level2_code=level2_code,
                                   level3_code=level3_code)

    def test_code_fields_do_not_accept_letters(self):
        """
            Test if a validation error occurs when a field that store a code
            tries to be saved with a letter or special char
        """
        cgce = self.create_cgce(level1_code="2k",
                                level2_code="d45",
                                level3_code="skdfj")
        with self.assertRaises(ValidationError) as cm:
            cgce.full_clean()

        self.assertTrue('level1_code' in cm.exception.message_dict and
                        "Somente números são permitidos" in
                        cm.exception.message_dict['level1_code'])
        self.assertTrue('level2_code' in cm.exception.message_dict and
                        "Somente números são permitidos" in
                        cm.exception.message_dict['level2_code'])
        self.assertTrue('level3_code' in cm.exception.message_dict and
                        "Somente números são permitidos" in
                        cm.exception.message_dict['level3_code'])


class CUCITests(TestCase):
    def create_cuci(self, item_code, subitem_code,
                    position_code, chapter_code):
        return CUCI.objects.create(item_code=item_code,
                                   subitem_code=subitem_code,
                                   position_code=position_code,
                                   chapter_code=chapter_code)

    def test_code_fields_do_not_accept_letters(self):
        """
            Test if a validation error occurs when a field that store a code
            tries to be saved with a letter or special char
        """
        cuci = self.create_cuci(item_code="2%",
                                subitem_code="&*45",
                                position_code="skdfj",
                                chapter_code="test")
        with self.assertRaises(ValidationError) as cm:
            cuci.full_clean()

        self.assertTrue('item_code' in cm.exception.message_dict and
                        "Somente números são permitidos" in
                        cm.exception.message_dict['item_code'])
        self.assertTrue('subitem_code' in cm.exception.message_dict and
                        "Somente números são permitidos" in
                        cm.exception.message_dict['subitem_code'])
        self.assertTrue('position_code' in cm.exception.message_dict and
                        "Somente números são permitidos" in
                        cm.exception.message_dict['position_code'])
        self.assertTrue('chapter_code' in cm.exception.message_dict and
                        "Somente números são permitidos" in
                        cm.exception.message_dict['chapter_code'])


class NCMTests(TestCase):

    def setUp(self):
        self.sh = SH.objects.create(
            chapter_code="32",
            chapter_name_pt="test",
            chapter_name_en="test",
            chapter_name_es="test",
            position_code="3215",
            position_name_pt="test",
            position_name_en="test",
            position_name_es="test",
            subposition_code="321574",
            subposition_name_pt="test",
            subposition_name_en="test",
            subposition_name_es="test",
            section_code="IV",
            section_name_pt="test",
            section_name_en="test",
            section_name_es="test"
        )

        self.cgce = CGCE.objects.create(
            level1_code="2",
            level1_name_pt="test",
            level1_name_en="test",
            level1_name_es="test",
            level2_code="23",
            level2_name_pt="test",
            level2_name_en="test",
            level2_name_es="test",
            level3_code="235",
            level3_name_pt="test",
            level3_name_en="test",
            level3_name_es="test"
        )

        self.cuci = CUCI.objects.create(
            item_code="12345",
            item_name_pt="test",
            item_name_en="test",
            item_name_es="test",
            subitem_code="1234",
            subitem_name_pt="test",
            subitem_name_en="test",
            subitem_name_es="test",
            position_code="123",
            position_name_pt="test",
            position_name_en="test",
            position_name_es="test",
            chapter_code="12",
            chapter_name_pt="test",
            chapter_name_en="test",
            chapter_name_es="test",
            section_code="XX",
            section_name_pt="test",
            section_name_en="test",
            section_name_es="test"
        )

    def create_ncm(self, ncm_code, ppe_code,
                   ppi_code, statistic_unit_code,
                   aggregate_factor_code,
                   isic4_code, siit_code):
        return NCM.objects.create(ncm_code=ncm_code, ppe_code=ppe_code,
                                  ppi_code=ppi_code,
                                  statistic_unit_code=statistic_unit_code,
                                  aggregate_factor_code=aggregate_factor_code,
                                  isic4_code=isic4_code, siit_code=siit_code,
                                  sh=self.sh, cgce=self.cgce, cuci=self.cuci,
                                  ncm_name_pt="test", ncm_name_en="test",
                                  ncm_name_es="test", exportation_subset="2")

    def test_code_fields_do_not_accept_letters(self):
        """
            Test if a validation error occurs when a field that store a code
            tries to be saved with a letter or special char
        """
        ncm = self.create_ncm(ncm_code="%321", ppe_code="kd9",
                              ppi_code="2#8",
                              statistic_unit_code="#@!9",
                              aggregate_factor_code="test",
                              isic4_code="$'od", siit_code="sadc")
        with self.assertRaises(ValidationError) as cm:
            ncm.full_clean()

        self.assertTrue('ncm_code' in cm.exception.message_dict and
                        "Somente números são permitidos" in
                        cm.exception.message_dict['ncm_code'])
        self.assertTrue('ppe_code' in cm.exception.message_dict and
                        "Somente números são permitidos" in
                        cm.exception.message_dict['ppe_code'])
        self.assertTrue('ppi_code' in cm.exception.message_dict and
                        "Somente números são permitidos" in
                        cm.exception.message_dict['ppi_code'])
        self.assertTrue('statistic_unit_code' in cm.exception.message_dict and
                        "Somente números são permitidos" in
                        cm.exception.message_dict['statistic_unit_code'])
        self.assertTrue('aggregate_factor_code' in cm.exception.message_dict
                        and "Somente números são permitidos" in
                        cm.exception.message_dict['aggregate_factor_code'])
        self.assertTrue('isic4_code' in cm.exception.message_dict and
                        "Somente números são permitidos" in
                        cm.exception.message_dict['isic4_code'])
        self.assertTrue('siit_code' in cm.exception.message_dict and
                        "Somente números são permitidos" in
                        cm.exception.message_dict['siit_code'])

    def test_cascade_delete_sh(self):
        self.create_ncm(ncm_code="123", ppe_code="32",
                        ppi_code="28",
                        statistic_unit_code="11",
                        aggregate_factor_code="2",
                        isic4_code="21", siit_code="4")
        self.sh.delete()

        with self.assertRaises(NCM.DoesNotExist):
            NCM.objects.get()

    def test_cascade_delete_cgce(self):
        self.create_ncm(ncm_code="123", ppe_code="32",
                        ppi_code="28",
                        statistic_unit_code="11",
                        aggregate_factor_code="2",
                        isic4_code="21", siit_code="4")
        self.cgce.delete()

        with self.assertRaises(NCM.DoesNotExist):
            NCM.objects.get()

    def test_cascade_delete_cuci(self):
        self.create_ncm(ncm_code="123", ppe_code="32",
                        ppi_code="28",
                        statistic_unit_code="11",
                        aggregate_factor_code="2",
                        isic4_code="21", siit_code="4")
        self.cuci.delete()

        with self.assertRaises(NCM.DoesNotExist):
            NCM.objects.get()


class AssetExportFactsTestModel(TestCase):

    def setUp(self):
        """
            This method will run before each test
        """

        self.tradeBlocs = TradeBlocs.objects.create(
            bloc_name_pt="portuguese",
            bloc_name_en="english",
            bloc_name_es="spanish",
            bloc_code="190"
        )

        self.country = Country.objects.create(
            country_name_pt="Nome",
            country_name_en="Name",
            country_name_es="Nombre",
            country_code_iso3="190",
            trade_bloc=self.tradeBlocs
        )

        self.federativeUnit = FederativeUnit.objects.create(
            uf_name="Name",
            uf_code="9090",
            uf_initials="SP"
        )

        self.urf = Urf.objects.create(
            urf_name="name",
            urf_code="code"
        )

        self.transportation = Transportation.objects.create(
            transportation_name="Name",
            transportation_code="code"
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
            bloc_name_pt="portuguese",
            bloc_name_en="english",
            bloc_name_es="spanish",
            bloc_code="190"
        )

        self.country = Country.objects.create(
            country_name_pt="Nome",
            country_name_en="Name",
            country_name_es="Nombre",
            country_code_iso3="190",
            trade_bloc=self.tradeBlocs
        )

        self.federativeUnit = FederativeUnit.objects.create(
            uf_name="Name",
            uf_code="9090",
            uf_initials="SP"
        )

        self.urf = Urf.objects.create(
            urf_name="name",
            urf_code="code"
        )

        self.transportation = Transportation.objects.create(
            transportation_name="Name",
            transportation_code="code"
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
            bloc_name_pt="portuguese",
            bloc_name_en="english",
            bloc_name_es="spanish",
            bloc_code="190"
        )

        self.country = Country.objects.create(
            country_name_pt="Nome",
            country_name_en="Name",
            country_name_es="Nombre",
            country_code_iso3="190",
            trade_bloc=self.tradeBlocs
        )

        self.federativeUnit = FederativeUnit.objects.create(
            uf_name="Name",
            uf_code="9090",
            uf_initials="SP"
        )

        self.urf = Urf.objects.create(
            urf_name="name",
            urf_code="code"
        )

        self.transportation = Transportation.objects.create(
            transportation_name="Name",
            transportation_code="code"
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
        '''
            This test verifies the database search result
        '''

        query = '''
          query {
            allImport{
              edges {
                node {
                  date
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
                    urfName
                    urfCode
                  }
                  transportation {
                    transportationName
                    transportationCode
                  }
                  registries
                  netKilogram
                  fobValue
                  destinationFedUnit {
                    ufName
                    ufCode
                    ufInitials
                  }
                  originCountry {
                    countryNamePt
                    countryNameEn
                    countryNameEs
                    countryCodeIso3
                    tradeBloc {
                      blocNamePt
                      blocNameEn
                      blocNameEs
                      blocCode
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
                                "urfName": "name",
                                "urfCode": "code"
                            },
                            "transportation": {
                                "transportationName": "Name",
                                "transportationCode": "code"
                            },
                            "registries": 1,
                            "netKilogram": 1.0,
                            "fobValue": 191.0,
                            "destinationFedUnit": {
                                "ufName": "Name",
                                "ufCode": "9090",
                                "ufInitials": "SP"
                            },
                            "originCountry": {
                                "countryNamePt": "Nome",
                                "countryNameEn": "Name",
                                "countryNameEs": "Nombre",
                                "countryCodeIso3": "190",
                                "tradeBloc": {
                                    "blocNamePt": "portuguese",
                                    "blocNameEn": "english",
                                    "blocNameEs": "spanish",
                                    "blocCode": "190"
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
        '''
            This test verifies the database search result
        '''

        query = '''
            query {
              allExport {
                edges {
                  node {
                    date
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
                      urfName
                      urfCode
                    }
                    transportation {
                      transportationName
                      transportationCode
                    }
                    registries
                    netKilogram
                    fobValue
                    originFedUnit {
                      ufName
                      ufCode
                      ufInitials
                    }
                    destinationCountry {
                      countryNamePt
                      countryNameEn
                      countryNameEs
                      countryCodeIso3
                      tradeBloc {
                        blocNamePt
                        blocNameEn
                        blocNameEs
                        blocCode
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
                                "urfName": "name",
                                "urfCode": "code"
                            },
                            "transportation": {
                                "transportationName": "Name",
                                "transportationCode": "code"
                            },
                            "registries": 1,
                            "netKilogram": 1.0,
                            "fobValue": 191.0,
                            "originFedUnit": {
                                "ufName": "Name",
                                "ufCode": "9090",
                                "ufInitials": "SP"
                            },
                            "destinationCountry": {
                                "countryNamePt": "Nome",
                                "countryNameEn": "Name",
                                "countryNameEs": "Nombre",
                                "countryCodeIso3": "190",
                                "tradeBloc": {
                                    "blocNamePt": "portuguese",
                                    "blocNameEn": "english",
                                    "blocNameEs": "spanish",
                                    "blocCode": "190"
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

    def test_query_trade_blocs(self):
        '''
            This test verifies the database search result
        '''

        query = '''
            query{
              allTradeblocs{
                edges{
                  node{
                    blocNamePt
                    blocNameEn
                    blocNameEs
                    blocCode
                  }
                }
              }
            }
        '''

        expected = {"allTradeblocs": {
                "edges": [
                    {
                        "node": {
                            "blocNamePt": "portuguese",
                            "blocNameEn": "english",
                            "blocNameEs": "spanish",
                            "blocCode": "190"
                        }
                    }
                ]
            }
         }

        schema = graphene.Schema(Query)
        result = schema.execute(query)
        self.assertEqual(expected, result.data)

    def test_query_country(self):
        '''
            This test verifies the database search result
        '''

        query = '''
            {
              allCountry{
                edges{
                  node{
                    countryNamePt
                    countryNameEn
                    countryNameEs
                    countryCodeIso3
                  }
                }
              }
            }
        '''

        expected = {"allCountry": {
                "edges": [
                    {
                        "node": {
                            "countryNamePt": "Nome",
                            "countryNameEn": "Name",
                            "countryNameEs": "Nombre",
                            "countryCodeIso3": "190",
                        }
                    }
                ]
            }
         }

        schema = graphene.Schema(Query)
        result = schema.execute(query)
        self.assertEqual(expected, result.data)

    def test_query_federative_unit(self):
        '''
            This test verifies the database search result
        '''

        query = '''
            {
              allFederativeunit{
                edges{
                  node{
                    ufName
                    ufCode
                    ufInitials
                  }
                }
              }
            }
        '''

        expected = {"allFederativeunit": {
                "edges": [
                    {
                        "node": {
                            "ufName": "Name",
                            "ufCode": "9090",
                            "ufInitials": "SP"
                        }
                    }
                ]
            }
         }

        schema = graphene.Schema(Query)
        result = schema.execute(query)
        self.assertEqual(expected, result.data)

    def test_query_transportation(self):
        '''
            This test verifies the database search result
        '''

        query = '''
            {
              allTransportation{
                edges{
                  node{
                    transportationName
                    transportationCode
                  }
                }
              }
            }
        '''

        expected = {"allTransportation": {
                "edges": [
                    {
                        "node": {
                            "transportationName": "Name",
                            "transportationCode": "code"
                        }
                    }
                ]
            }
         }

        schema = graphene.Schema(Query)
        result = schema.execute(query)
        self.assertEqual(expected, result.data)

    def test_query_urf(self):
        '''
            This test verifies the database search result
        '''

        query = '''
            {
              allUrf{
                edges{
                  node{
                    urfName
                    urfCode
                  }
                }
              }
            }
        '''

        expected = {"allUrf": {
                "edges": [
                    {
                        "node": {
                            "urfName": "name",
                            "urfCode": "code"
                        }
                    }
                ]
            }
         }

        schema = graphene.Schema(Query)
        result = schema.execute(query)
        self.assertEqual(expected, result.data)

    def test_query_range_date_import(self):

            '''
                This test verifies the range date search
            '''
            query = '''
                {
                allImport(commercializedBetween: "[\\"2018-01-01\\",\\"2018-12-31\\"]"){
                    edges{
                    node{
                        ncm{
                            ncmNamePt
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
                                "ncm":{
                                    "ncmNamePt": "Outras partes para motores de explosao"
                                }
                            }
                        }
                    ]
                }
            }
            schema = graphene.Schema(Query)
            result = schema.execute(query)
            self.assertEqual(expected, result.data)

    def test_query_range_date_export(self):
            '''
                This test verifies the range date search
            '''
            query = '''
                {
                    allExport(commercializedBetween: "[\\"2018-01-01s\\",\\"2018-12-31\\"]"){
                        edges{
                            node{
                                date
                            }
                        }
                    }
                }
            '''
            expected = {"allExport": {
                    "edges": [
                        {
                            "node": {
                                "date": "2018-09-21"
                            }
                        }
                    ]
                }
            }
            schema = graphene.Schema(Query)
            result = schema.execute(query)
            self.assertEqual(expected, result.data)

    def test_import_aggregated_fob_value_country(self):
        '''
            This test verifies the database search result
            for the aggregated searches
        '''

        query = '''
            {
                aggregatedImportCountry{
                    edges{
                        node{
                            originCountry{
                                countryNamePt
                            }
                            totalFobValueCountry
                        }
                    }
                }
            }
        '''

        expected = OrderedDict([('aggregatedImportCountry', OrderedDict([('edges', [OrderedDict([('node', OrderedDict([('originCountry', OrderedDict([('countryNamePt', 'Nome')])), ('totalFobValueCountry', '191.0')]))])])]))])

        schema = graphene.Schema(Query)
        result = schema.execute(query)
        self.assertEqual(expected, result.data)

    def test_import_aggregated_fob_value_date(self):
        '''
            This test verifies the database search result
            for the aggregated searches
        '''

        query = '''
            {
                aggregatedImportCountry{
                    edges{
                        node{
                            originCountry{
                                countryNamePt
                            }
                            totalFobValueDate
                        }
                    }
                }
            }
        '''

        expected = OrderedDict([('aggregatedImportCountry', OrderedDict([('edges', [OrderedDict([('node', OrderedDict([('originCountry', OrderedDict([('countryNamePt', 'Nome')])), ('totalFobValueDate', '191.0')]))])])]))])

        schema = graphene.Schema(Query)
        result = schema.execute(query)
        self.assertEqual(expected, result.data)

    def test_import_aggregated_fob_value_transportation(self):
        '''
            This test verifies the database search result
            for the aggregated searches
        '''

        query = '''
            {
                aggregatedImportCountry{
                    edges{
                        node{
                            originCountry{
                                countryNamePt
                            }
                            totalFobValueTransportation
                        }
                    }
                }
            }
        '''

        expected = OrderedDict([('aggregatedImportCountry', OrderedDict([('edges', [OrderedDict([('node', OrderedDict([('originCountry', OrderedDict([('countryNamePt', 'Nome')])), ('totalFobValueTransportation', '191.0')]))])])]))])

        schema = graphene.Schema(Query)
        result = schema.execute(query)
        self.assertEqual(expected, result.data)

    def test_import_aggregated_fob_value_urf(self):
        '''
            This test verifies the database search result
            for the aggregated searches
        '''

        query = '''
            {
                aggregatedImportCountry{
                    edges{
                        node{
                            originCountry{
                                countryNamePt
                            }
                            totalFobValueUrf
                        }
                    }
                }
            }
        '''

        expected = OrderedDict([('aggregatedImportCountry', OrderedDict([('edges', [OrderedDict([('node', OrderedDict([('originCountry', OrderedDict([('countryNamePt', 'Nome')])), ('totalFobValueUrf', '191.0')]))])])]))])

        schema = graphene.Schema(Query)
        result = schema.execute(query)
        self.assertEqual(expected, result.data)
    
    def test_import_aggregated_fob_value_trade_bloc(self):
        '''
            This test verifies the database search result
            for the aggregated searches
        '''

        query = '''
            {
                aggregatedImportCountry{
                    edges{
                        node{
                            originCountry{
                                countryNamePt
                            }
                            totalFobValueTradeBloc
                        }
                    }
                }
            }
        '''

        expected = OrderedDict([('aggregatedImportCountry', OrderedDict([('edges', [OrderedDict([('node', OrderedDict([('originCountry', OrderedDict([('countryNamePt', 'Nome')])), ('totalFobValueTradeBloc', '191.0')]))])])]))])

        schema = graphene.Schema(Query)
        result = schema.execute(query)
        self.assertEqual(expected, result.data)

    def test_import_aggregated_registries_country(self):
        '''
            This test verifies the database search result
            for the aggregated searches
        '''

        query = '''
            {
                aggregatedImportCountry{
                    edges{
                        node{
                            originCountry{
                                countryNamePt
                            }
                            totalRegistriesCountry
                        }
                    }
                }
            }
        '''

        expected = OrderedDict([('aggregatedImportCountry', OrderedDict([('edges', [OrderedDict([('node', OrderedDict([('originCountry', OrderedDict([('countryNamePt', 'Nome')])), ('totalRegistriesCountry', '1')]))])])]))])

        schema = graphene.Schema(Query)
        result = schema.execute(query)
        self.assertEqual(expected, result.data)

    def test_import_aggregated_registries_date(self):
        '''
            This test verifies the database search result
            for the aggregated searches
        '''

        query = '''
            {
                aggregatedImportCountry{
                    edges{
                        node{
                            originCountry{
                                countryNamePt
                            }
                            totalRegistriesDate
                        }
                    }
                }
            }
        '''

        expected = OrderedDict([('aggregatedImportCountry', OrderedDict([('edges', [OrderedDict([('node', OrderedDict([('originCountry', OrderedDict([('countryNamePt', 'Nome')])), ('totalRegistriesDate', '1')]))])])]))])

        schema = graphene.Schema(Query)
        result = schema.execute(query)
        self.assertEqual(expected, result.data)

    def test_import_aggregated_registries_transportation(self):
        '''
            This test verifies the database search result
            for the aggregated searches
        '''

        query = '''
            {
                aggregatedImportCountry{
                    edges{
                        node{
                            originCountry{
                                countryNamePt
                            }
                            totalRegistriesTransportation
                        }
                    }
                }
            }
        '''

        expected = OrderedDict([('aggregatedImportCountry', OrderedDict([('edges', [OrderedDict([('node', OrderedDict([('originCountry', OrderedDict([('countryNamePt', 'Nome')])), ('totalRegistriesTransportation', '1')]))])])]))])

        schema = graphene.Schema(Query)
        result = schema.execute(query)
        self.assertEqual(expected, result.data) 

    def test_import_aggregated_registries_urf(self):
        '''
            This test verifies the database search result
            for the aggregated searches
        '''

        query = '''
            {
                aggregatedImportCountry{
                    edges{
                        node{
                            originCountry{
                                countryNamePt
                            }
                            totalRegistriesUrf
                        }
                    }
                }
            }
        '''

        expected = OrderedDict([('aggregatedImportCountry', OrderedDict([('edges', [OrderedDict([('node', OrderedDict([('originCountry', OrderedDict([('countryNamePt', 'Nome')])), ('totalRegistriesUrf', '1')]))])])]))])

        schema = graphene.Schema(Query)
        result = schema.execute(query)
        self.assertEqual(expected, result.data) 

    def test_import_aggregated_registries_trade_bloc(self):
        '''
            This test verifies the database search result
            for the aggregated searches
        '''

        query = '''
            {
                aggregatedImportCountry{
                    edges{
                        node{
                            originCountry{
                                countryNamePt
                            }
                            totalRegistriesTradeBloc
                        }
                    }
                }
            }
        '''

        expected = OrderedDict([('aggregatedImportCountry', OrderedDict([('edges', [OrderedDict([('node', OrderedDict([('originCountry', OrderedDict([('countryNamePt', 'Nome')])), ('totalRegistriesTradeBloc', '1')]))])])]))])

        schema = graphene.Schema(Query)
        result = schema.execute(query)
        self.assertEqual(expected, result.data) 

    def test_import_aggregated_net_kilogram_date(self):
        '''
            This test verifies the database search result
            for the aggregated searches
        '''

        query = '''
            {
                aggregatedImportCountry{
                    edges{
                        node{
                            originCountry{
                                countryNamePt
                            }
                            totalNetKilogramDate
                        }
                    }
                }
            }
        '''

        expected = OrderedDict([('aggregatedImportCountry', OrderedDict([('edges', [OrderedDict([('node', OrderedDict([('originCountry', OrderedDict([('countryNamePt', 'Nome')])), ('totalNetKilogramDate', '1.0')]))])])]))])

        schema = graphene.Schema(Query)
        result = schema.execute(query)
        self.assertEqual(expected, result.data) 

    def test_import_aggregated_net_kilogram_country(self):
        '''
            This test verifies the database search result
            for the aggregated searches
        '''

        query = '''
            {
                aggregatedImportCountry{
                    edges{
                        node{
                            originCountry{
                                countryNamePt
                            }
                            totalNetKilogramCountry
                        }
                    }
                }
            }
        '''

        expected = OrderedDict([('aggregatedImportCountry', OrderedDict([('edges', [OrderedDict([('node', OrderedDict([('originCountry', OrderedDict([('countryNamePt', 'Nome')])), ('totalNetKilogramCountry', '1.0')]))])])]))])

        schema = graphene.Schema(Query)
        result = schema.execute(query)
        self.assertEqual(expected, result.data) 

    def test_import_aggregated_net_kilogram_transportation(self):
        '''
            This test verifies the database search result
            for the aggregated searches
        '''

        query = '''
            {
                aggregatedImportCountry{
                    edges{
                        node{
                            originCountry{
                                countryNamePt
                            }
                            totalNetKilogramTransportation
                        }
                    }
                }
            }
        '''

        expected = OrderedDict([('aggregatedImportCountry', OrderedDict([('edges', [OrderedDict([('node', OrderedDict([('originCountry', OrderedDict([('countryNamePt', 'Nome')])), ('totalNetKilogramTransportation', '1.0')]))])])]))])

        schema = graphene.Schema(Query)
        result = schema.execute(query)
        self.assertEqual(expected, result.data) 

    def test_import_aggregated_net_kilogram_urf(self):
        '''
            This test verifies the database search result
            for the aggregated searches
        '''

        query = '''
            {
                aggregatedImportCountry{
                    edges{
                        node{
                            originCountry{
                                countryNamePt
                            }
                            totalNetKilogramUrf
                        }
                    }
                }
            }
        '''

        expected = OrderedDict([('aggregatedImportCountry', OrderedDict([('edges', [OrderedDict([('node', OrderedDict([('originCountry', OrderedDict([('countryNamePt', 'Nome')])), ('totalNetKilogramUrf', '1.0')]))])])]))])

        schema = graphene.Schema(Query)
        result = schema.execute(query)
        self.assertEqual(expected, result.data) 

    def test_import_aggregated_net_kilogram_trade_bloc(self):
        '''
            This test verifies the database search result
            for the aggregated searches
        '''

        query = '''
            {
                aggregatedImportCountry{
                    edges{
                        node{
                            originCountry{
                                countryNamePt
                            }
                            totalNetKilogramTradeBloc
                        }
                    }
                }
            }
        '''

        expected = OrderedDict([('aggregatedImportCountry', OrderedDict([('edges', [OrderedDict([('node', OrderedDict([('originCountry', OrderedDict([('countryNamePt', 'Nome')])), ('totalNetKilogramTradeBloc', '1.0')]))])])]))])

        schema = graphene.Schema(Query)
        result = schema.execute(query)
        self.assertEqual(expected, result.data) 

