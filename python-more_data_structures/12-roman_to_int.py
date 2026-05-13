#!/usr/bin/python3
def roman_to_int(roman_string):
    roman_dict = {"M": 1000, "C": 100, "D": 500, "X": 10, "L": 50, "I": 1, "V": 5}
    if roman_string is not None and type(roman_string) == str:
        number = 0
        for i in range(0, len(roman_string)):
            if i == len(roman_string) - 1:
                number = number + roman_dict[roman_string[i]]
            elif roman_dict[roman_string[i]] > roman_dict[roman_string[i + 1]]:
                number = number + roman_dict[roman_string[i]]
            elif roman_dict[roman_string[i]] < roman_dict[roman_string[i + 1]]:
                number = number - roman_dict[roman_string[i]]
            else:
                number = number + roman_dict[roman_string[i]]
        return number
    return 0
