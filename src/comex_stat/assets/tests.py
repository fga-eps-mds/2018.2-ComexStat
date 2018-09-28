from django.test import TestCase
from comex_stat.assets.models import CUCI, NCM, SH, CGCE
from django.core.exceptions import ValidationError
# Create your tests here.


class SHTests(TestCase):
    def create_sh(self, chapter_code, position_code, subposition_code):
        return SH.objects.create(chapter_code=chapter_code,
                                 position_code=position_code,
                                 subposition_code=subposition_code)

    def test_code_fields_do_not_accept_letters(self):
        """
            Test if the fields that store codes does not accept letters or
            special chars in it
        """
        sh = self.create_sh(chapter_code="a", position_code="4%3",
                            subposition_code="1-+=3")
        with self.assertRaises(ValidationError) as cm:
            sh.full_clean()

        self.assertTrue('chapter_code' in cm.exception.message_dict)
        self.assertTrue('position_code' in cm.exception.message_dict)
        self.assertTrue('subposition_code' in cm.exception.message_dict)


class CGCETests(TestCase):
    def create_cgce(self, level1_code, level2_code, level3_code):
        return CGCE.objects.create(level1_code=level1_code,
                                   level2_code=level2_code,
                                   level3_code=level3_code)

    def test_code_fields_do_not_accept_letters(self):
        """
            Test if the fields that store codes does not accept letters or
            special chars in it
        """
        cgce = self.create_cgce(level1_code="2k",
                                level2_code="d45",
                                level3_code="skdfj")
        with self.assertRaises(ValidationError) as cm:
            cgce.full_clean()

        self.assertTrue('level1_code' in cm.exception.message_dict)
        self.assertTrue('level2_code' in cm.exception.message_dict)
        self.assertTrue('level3_code' in cm.exception.message_dict)


class CUCITests(TestCase):
    def create_cuci(self, item_code, subitem_code,
                    position_code, chapter_code):
        return CUCI.objects.create(item_code=item_code,
                                   subitem_code=subitem_code,
                                   position_code=position_code,
                                   chapter_code=chapter_code)

    def test_code_fields_do_not_accept_letters(self):
        """
            Test if the fields that store codes does not accept letters or
            special chars in it
        """
        cuci = self.create_cuci(item_code="2%",
                                subitem_code="&*45",
                                position_code="skdfj",
                                chapter_code="test")
        with self.assertRaises(ValidationError) as cm:
            cuci.full_clean()

        self.assertTrue('item_code' in cm.exception.message_dict)
        self.assertTrue('subitem_code' in cm.exception.message_dict)
        self.assertTrue('position_code' in cm.exception.message_dict)
        self.assertTrue('chapter_code' in cm.exception.message_dict)
