#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Author: Khoo Zhenyu
Student ID: 2600220458-3
Program description: This program is a simple program that reads a file
and converts the file into a NumPy array. From there, it also creates
a 1-D array of 30 values. The program then combines that array and the array
from the file. After that, it creates a random 1-D array with 30 random
values. The program then combines that array and the previously made array.
It then gets the average of the first 1-D array and the sum of the second 1-D
array.

"""

import numpy as np
from numpy import random

def make_array(filename):
    """
    Reads a file, and then converts the string elements into floating
    point numbers by creating an empty list and using a for loop to populate it.
    The function then returns the array.
    """
    with open(filename, 'r', encoding='utf-8') as f:
        textarray = f.read().splitlines()
        lst = []
        for i in textarray:
            floats = float(i)
            lst.append(floats)
        return np.array(lst)

read_arr = make_array("numbers.txt")
print("Array created from the numbers of the text file:", read_arr)
print("Type of read_arr:", type(read_arr))

# Creates a 1D NumPy array with 30 values spaced linearly from 5 to 100
arr_1 = np.linspace(5, 100, num = 30)
print("\nArray created with 30 values spaced linearly from 5 to 100:", arr_1)

# arr_1 is redefinied as arr_1 + read_arr
arr_1 = arr_1 + read_arr

# Create a 1D number random array with 30 floating point numbers
arr_2 = random.rand(30)

# Join the arrays arr_1 and arr_2 along axis 0 using np.stack()
stacked_array = np.stack((arr_1, arr_2), axis=0)
print("\nStacked array:", stacked_array)

# Average of the first 1-D array
average = np.mean(stacked_array[0])
print("\nAverage of the stacked array[0]:", average)

# Summation of the first 5 elements of the second 1-D array
summa = np.sum(stacked_array[1][0:5])
print("\nSum of the first 5 elements of stacked_array[1]:", summa)
