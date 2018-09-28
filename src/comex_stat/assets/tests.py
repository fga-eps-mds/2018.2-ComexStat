from django.test import TestCase
from comex_stat.assets.models import CUCI, NCM, SH, CGCE
from django.core.exceptions import ValidationError


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
