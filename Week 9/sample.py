# from telnetlib import OUTMRK


# def return_number():
#     return 5

# print("Calling the function:", return_number())
# print("Calling the function and multiplying the return value by 6:", return_number() * 6)
# x = return_number()
# y = x**2
# print(y)

# def multiply(x, y):
#     z = x * y

# our_value = multiply(3, 4)
# print(our_value)

# def operation(x, y):
#     z = x*y
#     n = y**2
#     return z, n

# number_1, number_2 = operation(3, 4)
# print(number_1)
# print(number_2)

# def is_even(n):
#     if n % 2 == 0:
#         return print("The number is even")
#     else:
#         return print("The number is odd")

# is_even(41)
# is_even(42)                         

# def is_divisible(x, y):
#     if x % y == 0 :
#         return True
#     return False

# boolean = is_divisible(4, 2)
# print(boolean)

# def f():
#     n = 5
#     return n*2

# print("Calling function f and printing the return value:", f())
# # print(n) won't print as it is not defined

# def function_f():
#     n = 5
#     print(n)

# def function_g():
#     n = "Just a string"
#     print(n)

# print("Calling function_f:")
# function_f()
# print("Calling function_g:")
# function_g()

# x = 7

# def function_f(y):
#     x = 3
#     return (y*3)
# print("Calling function_f and printing the return value:", function_f(3))
# print(x)

# n = 0
# def add(x):
#     n += x

# add(3)

n = 5555
print(id(n))
n += 3
print(id(n))