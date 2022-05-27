#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Author: Khoo Zhenyu
Student ID: 2600220458-3
Program description:

"""

num_lst = [[1,1,4,66],[-55,7],[-1,43,55,-6,12,12,4]]

even_numbers = []
odd_numbers = []

def flatten_list(a_list):
    """Flattens the list - makes a normal lsit from a nested list."""
    flat_num_lst = []
    for lst in a_list:
        for element in lst:
            flat_num_lst.append(element)

    return flat_num_lst

def filter_numbers(number_list, evens = even_numbers, odds = odd_numbers):
    """Filters the numbers in a list and stores them in two lists."""
    for i in number_list:
        if i > 0:
            if i % 2 == 0:
                evens.append(i)
            else:
                odds.append(i)

def remove_dups(a_list):
    """Removes duplicates from a list"""
    dups_removed = list(dict.fromkeys(a_list))
    return dups_removed
    
flat_num_lst = flatten_list(num_lst)
print(flat_num_lst)

filter_numbers(flat_num_lst)
print(even_numbers)
print(odd_numbers)

uen = remove_dups(even_numbers)
uon = remove_dups(odd_numbers)
print(uen)
print(uon)