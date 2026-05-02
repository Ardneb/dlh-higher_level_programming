#!/usr/bin/python3
def print_last_digit(number):
    last_digit = number % 10
    if number < 0 and last_digit != 0:
        return last_digit - 10
    else:
        return last_digit
