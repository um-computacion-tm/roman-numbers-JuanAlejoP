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
