import numpy as np
from numpy import random

def make_array(filename):
    """
    Reads a file and returns a numpy array
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

print("\narr1:" , arr_1)
print("\narr2:" , arr_2)

# join the arrays arr_1 and arr_2 along axis 0 using np.stack()
stacked_array = np.stack((arr_1, arr_2), axis=0)
print("\nStacked array:", stacked_array)

average = np.mean(stacked_array[0], axis=0)
print("\nAverage of the stacked array[0]:", average)

summa = np.sum(stacked_array[1], axis=0)
print("\nSum of the stacked array[0]:", summa)