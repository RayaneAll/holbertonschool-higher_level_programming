#!/usr/bin/python3
def roman_to_int(roman_string):
    roman_numeral = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }
    total = 0
    previous_value = 0
    for numeral in reversed(roman_string):
        current_value = roman_numeral[numeral]
    if current_value >= previous_value:
        total += current_value
    else:
        total -= current_value
    previous_value = current_value
    return total
