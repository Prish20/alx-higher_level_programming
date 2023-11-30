#!/usr/bin/python3

import random

def get_last_digit(number):
    return abs(number) % 10

number = random.randint(-10000, 10000)
last_digit = get_last_digit(number)

if last_digit > 5:
    print(f"Last digit of {number} is {last_digit} and is greater than 5")
elif last_digit == 0:
    print(f"Last digit of {number} is {last_digit} and is 0")
else:
    print(f"Last digit of {number} is {last_digit} and is less than 6 and not 0")
