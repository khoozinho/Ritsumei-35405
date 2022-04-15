#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Author: Khoo Zhenyu
Student ID: 2600220458-3
Program: Practicing variable assignment, type checking, operators,
and string methods
"""

# Variable assignment and print the result of the average.
num_1 = 10
num_2 = 20
num_3 = 31
average = (num_1 + num_2 + num_3) / 3
print(average)

# Print the data type of variable average.
print(type(average))

# Change statement into false in 2 different ways.
print(num_1 > num_2)
print(num_1 == num_2)

# Assign string to variable and print.
string_0 = "I don't know much about programming yet."
print(string_0)

# Indexing.
print('The 4th character is "' + string_0[3] + '".')

# Print length.
my_string = "apples"
print(len(my_string))

# .format method
print("Nikola Tesla was a Serbian-American {}, electrical engineer, {}.".format('inventor', 'mechanical engineer'))

blank1 = 'inventor'
blank2 = 'mechanical engineer'

print(f"Nikola Tesla was a Serbian-American {blank1}, electrical engineer, {blank2}.")
