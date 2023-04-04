import unittest
from main_dtr import decimal_to_roman
from main_rtd import roman_to_decimal


class TestDecimalToRoman(unittest.TestCase):

    def test_1(self):
        result = decimal_to_roman(1)
        self.assertEqual(result, 'I')

    def test_2(self):
        result = decimal_to_roman(2)
        self.assertEqual(result, 'II')

    def test_3(self):
        result = decimal_to_roman(3)
        self.assertEqual(result, 'III')

    def test_4(self):
        result = decimal_to_roman(4)
        self.assertEqual(result,'IV')

    def test_5(self):
        result = decimal_to_roman(5)
        self.assertEqual(result, 'V')

    def test_6(self):
        result = decimal_to_roman(6)
        self.assertEqual(result, 'VI')
    
    def test_9(self):
        result = decimal_to_roman(9)
        self.assertEqual(result, 'IX')

    def test_10(self):
        result = decimal_to_roman(10)
        self.assertEqual(result, 'X')

    def test_11(self):
        result = decimal_to_roman(11)
        self.assertEqual(result, 'XI')

    def test_12(self):
        result = decimal_to_roman(12)
        self.assertEqual(result, 'XII')

    def test_17(self):
        result = decimal_to_roman(17)
        self.assertEqual(result, 'XVII')

    def test_19(self):
        result = decimal_to_roman(19)
        self.assertEqual(result, 'XIX')

    def test_20(self):
        result = decimal_to_roman(20)
        self.assertEqual(result, 'XX')

    def test_21(self):
        result = decimal_to_roman(21)
        self.assertEqual(result, 'XXI')

    def test_24(self):
        result = decimal_to_roman(24)
        self.assertEqual(result, 'XXIV')

    def test_30(self):
        result = decimal_to_roman(30)
        self.assertEqual(result, 'XXX')

    def test_35(self):
        result = decimal_to_roman(35)
        self.assertEqual(result, 'XXXV')

    def test_38(self):
        result = decimal_to_roman(38)
        self.assertEqual(result, 'XXXVIII')

    def test_40(self):
        result = decimal_to_roman(40)
        self.assertEqual(result, 'XL')
    
    def test_47(self):
        result = decimal_to_roman(47)
        self.assertEqual(result, 'XLVII')

    def test_52(self):
        result = decimal_to_roman(52)
        self.assertEqual(result, 'LII')

    def test_66(self):
        result = decimal_to_roman(66)
        self.assertEqual(result, 'LXVI')
    
    def test_70(self):
        result = decimal_to_roman(70)
        self.assertEqual(result, 'LXX')

    def test_81(self):
        result = decimal_to_roman(81)
        self.assertEqual(result, 'LXXXI')
    
    def test_99(self):
        result = decimal_to_roman(99)
        self.assertEqual(result, 'XCIX')
    
    def test_100(self):
        result = decimal_to_roman(100)
        self.assertEqual(result, 'C')

    def test_102(self):
        result = decimal_to_roman(102)
        self.assertEqual(result, 'CII')

    def test_457(self):
        result = decimal_to_roman(457)
        self.assertEqual(result, 'CDLVII')

    def test_500(self):
        result = decimal_to_roman(500)
        self.assertEqual(result, 'D')

    def test_504(self):
        result = decimal_to_roman(504)
        self.assertEqual(result, 'DIV')

    def test_692(self):
        result = decimal_to_roman(692)
        self.assertEqual(result, 'DCXCII')

    def test_747(self):
        result = decimal_to_roman(747)
        self.assertEqual(result, 'DCCXLVII')

    def test_826(self):
        result = decimal_to_roman(826)
        self.assertEqual(result, 'DCCCXXVI')

    def test_999(self):
        result = decimal_to_roman(999)
        self.assertEqual(result, 'CMXCIX')

    def test_1000(self):
        result = decimal_to_roman(1000)
        self.assertEqual(result, 'M')


class TestRomanToDecimal(unittest.TestCase):

    def test_I(self):
        decimal = roman_to_decimal('I')
        self.assertEqual(decimal, 1)

    def test_II(self):
        decimal = roman_to_decimal('II')
        self.assertEqual(decimal, 2)
    
    def test_III(self):
        decimal = roman_to_decimal('III')
        self.assertEqual(decimal, 3)

    def test_IV(self):
        decimal = roman_to_decimal('IV')
        self.assertEqual(decimal, 4)

    def test_V(self):
        decimal = roman_to_decimal('V')
        self.assertEqual(decimal, 5)

    def test_VII(self):
        decimal = roman_to_decimal('VII')
        self.assertEqual(decimal, 7)

    def test_IX(self):
        decimal = roman_to_decimal('IX')
        self.assertEqual(decimal, 9)

    def test_X(self):
        decimal = roman_to_decimal('X')
        self.assertEqual(decimal, 10)

    def test_XI(self):
        decimal = roman_to_decimal('XI')
        self.assertEqual(decimal, 11)

    def test_XII(self):
        decimal = roman_to_decimal('XII')
        self.assertEqual(decimal, 12)

    def test_XVIII(self):
        decimal = roman_to_decimal('XVIII')
        self.assertEqual(decimal, 18)

    def test_XIX(self):
        decimal = roman_to_decimal('XIX')
        self.assertEqual(decimal, 19)

    def test_XX(self):
        decimal = roman_to_decimal('XX')
        self.assertEqual(decimal, 20)

    def test_XXI(self):
        decimal = roman_to_decimal('XXI')
        self.assertEqual(decimal, 21)

    def test_XXIII(self):
        decimal = roman_to_decimal('XXIII')
        self.assertEqual(decimal, 23)
        
    def test_XXX(self):
        decimal = roman_to_decimal('XXX')
        self.assertEqual(decimal, 30)

    def test_XXXV(self):
        decimal = roman_to_decimal('XXXV')
        self.assertEqual(decimal, 35)
    
    def test_XXXVII(self):
        decimal = roman_to_decimal('XXXVII')
        self.assertEqual(decimal, 37)

    def test_XL(self):
        decimal = roman_to_decimal('XL')
        self.assertEqual(decimal, 40)

    def test_XLVI(self):
        decimal = roman_to_decimal('XLVI')
        self.assertEqual(decimal, 46)
    
    def test_LIII(self):
        decimal = roman_to_decimal('LIII')
        self.assertEqual(decimal, 53)

    def test_LXVIII(self):
        decimal = roman_to_decimal('LXVIII')
        self.assertEqual(decimal, 68)
    
    def test_LXX(self):
        decimal = roman_to_decimal('LXX')
        self.assertEqual(decimal, 70)

    def test_LXXXIII(self):
        decimal = roman_to_decimal('LXXXIII')
        self.assertEqual(decimal, 83)

    def test_XCIX(self):
        decimal = roman_to_decimal('XCIX')
        self.assertEqual(decimal, 99)

    def test_C(self):
        decimal = roman_to_decimal('C')
        self.assertEqual(decimal, 100)

    def test_CII(self):
        decimal = roman_to_decimal('CII')
        self.assertEqual(decimal, 102)
    
    def test_CDLVII(self):
        decimal = roman_to_decimal('CDLVII')
        self.assertEqual(decimal, 457)

    def test_D(self):
        decimal = roman_to_decimal('D')
        self.assertEqual(decimal, 500)

    def test_DIV(self):
        decimal = roman_to_decimal('DIV')
        self.assertEqual(decimal, 504)

    def test_DCXCIII(self):
        decimal = roman_to_decimal('DCXCIII')
        self.assertEqual(decimal, 693)

    def test_DCCXLVIII(self):
        decimal = roman_to_decimal('DCCXLVIII')
        self.assertEqual(decimal, 748)

    def test_DCCCXXVI(self):
        decimal = roman_to_decimal('DCCCXXVI')
        self.assertEqual(decimal, 826)

    def test_CMXLIX(self):
        decimal = roman_to_decimal('CMXLIX')
        self.assertEqual(decimal, 949)

    def test_CMXCIX(self):
        decimal = roman_to_decimal('CMXCIX')
        self.assertEqual(decimal, 999)

    def test_M(self):
        decimal = roman_to_decimal('M')
        self.assertEqual(decimal, 1000)


if __name__ == '__main__':
    unittest.main()