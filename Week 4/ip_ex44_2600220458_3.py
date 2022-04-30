#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Author: Khoo Zhenyu
Student ID: 2600220458-3
Program description: Sums the parallel values of both lists, up till when the sum hits 25.

"""

number_list_1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
number_list_2 = [10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

print("Length of the first list: ", len(number_list_1))
print("Length of the second list: ", len(number_list_2))
for n1, n2 in zip(number_list_1, number_list_2):
    summa = n1 + n2
    print("The sum is", summa)
    if summa > 25:
        print("The sum is greater than 25")
        break

print("The loop has ended.")