import unittest

def roman_to_decimal(roman):

    decimal = 0
    roman01 = ''

    for letter in roman:
        if letter == 'I':
            decimal += 1
        if letter == 'V':
            if roman01 == 'I':
                decimal -= 2
            decimal += 5
        if letter == 'X':
            if roman01 == 'I':
                decimal -= 2
            decimal += 10
        if letter == 'L':
            if roman01 == 'X':
                decimal -= 20
            decimal += 50
        if letter == 'C':
            if roman01 == 'X':
                decimal -= 20
            decimal += 100
        if letter == 'D':
            if roman01 == 'C':
                decimal -= 200
            decimal += 500
        if letter == 'M':
            if roman01 == 'C':
                decimal -= 200
            decimal += 1000
        roman01 = letter
    return decimal


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