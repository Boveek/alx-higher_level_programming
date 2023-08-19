#!/usr/bin/python3
def roman_to_int(roman_string):
    roman_value = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
            }
    if not isinstance(roman_string, str) or roman_string is None:
        return 0
    num = len(roman_string)
    summ = 0
    for n in range(num - 1):
        if (roman_value[roman_string[n]] < roman_value[roman_string[n + 1]]):
            summ -= roman_value[roman_string[n]]
        else:
            summ += roman_value[roman_string[n]]
    summ += roman_value[roman_string[num - 1]]
    return summ
