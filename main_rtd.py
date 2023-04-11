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
