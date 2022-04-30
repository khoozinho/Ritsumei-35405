#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Author: Khoo Zhenyu
Student ID: 2600220458-3
Program description: This program sums up all even numbers from 1 up to and including 300.

"""

# Variables
number = 1
total = 0

# Main program
while number > 0:
    if (number % 2) == 0:
        total += number
        if number == 300:
            break
    number += 1

print('The total sum of the numbers is {}.'.format(total))