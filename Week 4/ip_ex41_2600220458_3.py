#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Author: Khoo Zhenyu
Student ID: 2600220458-3
Program description: This program reflects the grade based on the points given.

"""

print('Welcome to the grade criteria calculator. Please enter your score.')

points = 87

if points >= 90:
    print('You got an A+.')
elif points >= 80:
    print('You got an A.')
elif points >= 70:
    print('You got a B.')
elif points >= 60:
    print('You got a C.')
elif points < 60:
    print('You got an F.')