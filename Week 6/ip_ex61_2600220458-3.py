#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Author: Khoo Zhenyu
Student ID: 2600220458-3
Program description:

The initial portion is to create a couple of lists and then
combining them into a list, and then adding a third list into the same list using
the .append method. The following portion is to print the length of the list and 
reversing it.

A dictionary is also made and enumeration was used. There is also additions
made to the dictionary by using the .update method.

Lastly, the index list is sliced and the values put in a list, of which one is
popped and the rest filtered, and the largest value in the list is picked out
using the max function.

"""
# The two scientist lists.
scientist_list_1 = ['Einstein','Curie', 'Newton', 'Darwin']
scientist_list_2 = ['Tesla', 'Galilei', 'Lovelace']

scientist_list = scientist_list_1 + scientist_list_2

# The third scientist list.
scientist_list_3 = ['Hawking', 'Faraday']
for scientist in scientist_list_3:
    scientist_list.append(scientist)

# Printing length of list.
print("Length of the scientist list:", len(scientist_list))

# Reversing the list.
scientist_list.reverse()
print("Reversed scientist list:", scientist_list)

scientist_dict = {}

# Adding indicies and name of scientists to the dictionary.
for i, scientist in enumerate(scientist_list):
    scientist_dict[scientist] = i

print("The scientist dictionary:", scientist_dict)

# Addidition of scientist_dict_2
scientist_dict_2 = {
    "Faraday": 1,
    "Boyle": 9
}
scientist_dict.update(scientist_dict_2)

# Reprinting of scientist dictionary.
print("Scientist dictionary:", scientist_dict)

# Honestly not sure what to call this function.
index_list = list(scientist_dict.values())
print("Index list:", index_list)

# Slicing of the list.
numbers = index_list[0:5]
print("Numbers list:", numbers)

one = numbers.pop(0)

# Using for loop to remove odd numbers
for number in numbers:
    if (number % 2) != 0:
        numbers.remove(number)

# Printing number list without the odd numbers.
print("The numbers list filtered out of odd numbers:", numbers)

# Print maximum value of number list.
print("The maximum value in the numbers list:", max(numbers))
