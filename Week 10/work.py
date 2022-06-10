import numpy as np
from numpy import random

def make_array(filename):
    """
    Reads a file and returns a numpy array
    """
    with open(filename, 'r', encoding='utf-8') as f:
        textarray = f.read().splitlines()
    return np.array(textarray)

read_arr = make_array("numbers.txt")
print("Array created from the numbers of the text file:", read_arr)
print("Type of read_arr:", type(read_arr))

# Creates a 1D NumPy array with 30 values spaced linearly from 5 to 100
arr_1 = np.linspace(5, 100, num = 30)
print("\nArray created with 30 values spaced linearly from 5 to 100:", arr_1)

# arr_1 is redefinied as arr_1 + read_arr
arr_1 = np.concatenate((arr_1, read_arr))

# Create a 1D number random array with 30 floating point numbers
arr_2 = random.rand(30)

print("\narr1:" , arr_1)
print("Type of arr1:", type(arr_1))
print("\narr2:" , arr_2)
print("Type of arr2:", type(arr_2))

# stacked_array = np.stack((arr_1, arr_2), axis=0)
# print("Stacked array:", stacked_array)