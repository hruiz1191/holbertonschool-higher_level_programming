#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
lastn = number % 10
if lastn > 5:
    print(f"Last digit of {number} is {lastn} greater than 5")
elif lastn < 6 and lastn != 0:
    print(f"Last digit of {number} is less than  6 ans is not 0")
else:
    print(f"Last digit of {number} is {lastn} and is 0")
