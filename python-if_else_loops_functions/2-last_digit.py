#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
num_str = repr(number)
last_digit_str = num_str[-1]
last_digit = int(last_digit_str)
if last_digit >5:
    print(f"The last digit of {number} is {last_digit} and greater than 5")
if last_digit ==0:
    print(f"The last digit of {number} is {last_digit} and is 0")
if (last_digit <6) and (last_digit !=0):
    print(f"The last digit of {number} is {last_digit} and is less than 6 and not 0")