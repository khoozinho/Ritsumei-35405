#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Author: Khoo Zhenyu
Student ID: 2600220458-3
Program description: This program takes a nested list, and flattens it.
It also filters and removes out negative numbers, and separates
the remaining positive numbers into even and odd lists. It also removes
duplicates from both lists.

"""
# Lists
num_lst = [[1,1,4,66],[-55,7],[-1,43,55,-6,12,12,4]]
even_numbers = []
odd_numbers = []

# Functions
def flatten_list(a_list):
    """Flattens the list - makes a normal list from a nested list."""
    flat_num_lst = []
    for lst in a_list:
        for element in lst:
            flat_num_lst.append(element)

    return flat_num_lst

def filter_numbers(number_list, evens = even_numbers, odds = odd_numbers):
    """Filters the numbers in a list and stores them in two lists,
    odd and even numebers. It takes 3 arguments, the number list,
    the even numbers and odd numbers."""
    for i in number_list:
        if i > 0:
            if i % 2 == 0:
                evens.append(i)
            else:
                odds.append(i)

def remove_dups(a_list):
    """Removes duplicates from a list."""
    dups_removed = list(dict.fromkeys(a_list))
    return dups_removed

# Original list    
print("Original nested list:", num_lst)

# Flattens the list
flat_num_lst = flatten_list(num_lst)
print("Flattened list:", flat_num_lst)

# Filters the numbers in the list and stores them in odd and even lists
filter_numbers(flat_num_lst)
print("The even numbers:", even_numbers)
print("The odd numbers:", odd_numbers)

# Removal of duplicates and prints the lists
uniq_even_numbers = remove_dups(even_numbers)
uniq_odd_numbers = remove_dups(odd_numbers)
print("The unique even numbers:", uniq_even_numbers)
print("The unique odd numbers:", uniq_odd_numbers)