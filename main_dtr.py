import unittest


def decimal_to_roman(decimal):
    roman01 = ''
    roman02 = ''
    roman03 = ''
    roman04 = ''
    decimal_unit = (decimal%10)
    decimal_ten = (decimal%100 - decimal%10)//10
    decimal_hundred = (decimal%1000 - decimal%100)//100
    decimal_thousand = (decimal%10000 - decimal%1000)//1000

    if decimal:
        for digit in range(decimal_thousand):
            if decimal_thousand < 4:
                roman04 += 'M'

        for digit in range(decimal_hundred):
            if decimal_hundred < 4:
                roman01 += 'C'
            elif decimal_hundred == 4:
                roman01 = 'CD'
            elif 9 > decimal_hundred > 4:
                roman01 = 'C'*(decimal_hundred - 5)
                roman01 = 'D' + roman01
            elif decimal_hundred == 9:
                roman01 = 'CM'

        for digit in range(decimal_ten):
            if decimal_ten < 4:
                roman02 += 'X'
            elif decimal_ten == 4:
                roman02 = 'XL'
            elif 9 > decimal_ten > 4:
                roman02 = 'X'*(decimal_ten - 5)
                roman02 = 'L' + roman02
            elif decimal_ten == 9:
                roman02 = 'XC'

        for digit in range(decimal_unit):
            if decimal_unit < 4:
                roman03 += 'I'
            elif decimal_unit == 4:
                roman03 = 'IV'
            elif 9 > decimal_unit > 4:
                roman03 = 'I'*(decimal_unit - 5)
                roman03 = 'V' + roman03
            elif decimal_unit == 9:
                roman03 = 'IX'

    roman = roman04 + roman01 + roman02 + roman03

    return roman


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


if __name__ == '__main__':
    unittest.main()