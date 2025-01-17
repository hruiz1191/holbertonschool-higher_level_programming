#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)

if number < 0 and number != 0:
    lastn = -(-number % 10)
else:
    lastn = number % 10

if lastn == 0:
    print(f"Last digit of {number} is {lastn} and is 0")
elif lastn > 5:
    print(f"Last digit of {number} is {lastn} and is greater than 5")
else:
    print(f"Last digit of {number} is {lastn} is less than 6 and not 0")
