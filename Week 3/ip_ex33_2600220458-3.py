#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Author: Khoo Zhenyu
Student ID: 2600220458-3
Program description: Program that checks how many times the power can be raised before reaching the limit.

"""

# Exercise 3.3

# Variables
iterations = 0
number = 4

# While loop
while number < 100000:
    print(number)
    number = 2**number
    iterations += 1

# Print iterations
print(f"It took this many iterations: {iterations}")