#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Author: Khoo Zhenyu
Student ID: 2600220458-3
Program description: This program runs a simulation of 4 adventurers and 1 healer.
There is usage of object-oriented programming. In this program, there is the 'Adventurer'
class, as wekk as the 'Healer' class. The 'Adventurer' class has the 'intro' function and 
the 'need heals' function. The 'Healer' class has the 'healer_intro' function and the 'heal'
function. The 'run' function is the main function of the program. It checks the status of the
adventurer, and whether they need to be healed. If they need to be healed, the healer will
heal them, using up his medicine stock. The 'run' function will also print the status of the
adventurer.
"""

from numpy import random


class Adventurer:
    """
    Instansitate of the Adventurer class defines an object with class
    attribute maximum health, and instance attributes name and (current) health.
    An Adventurer can introduce itself, and has an instance method that decides 
    if the Adventurer needs healing or not.
    """
    max_health = 100

    def __init__(self, name):
        self.name = name
        self.health = random.randint(60, 91)

    def intro(self):
        """
        Adventurer introduction.
        Returns a string.
        """
        print(f"Hello my name is {self.name}!")

    def needs_heal(self):
        """
        Checks if the Adventurer needs healing (less than 80%).
        Return a boolean.
        """
        if self.health < 80:
            print("I need healing!")
            return True
        else:
            print("I'm fine!")
            return False


class Healer(Adventurer):
    """
    The Healer class inherits from the Adventurer class.
    The Healer class has an instance method that heals the Adventurer.
    """

    def __init__(self, name, medicine_stock):
        super().__init__(name)
        self.medicine_stock = medicine_stock

    def healer_intro(self):
        """
        Gives an introduction of the Healer.
        Uses the Adventurer introduction method.
        Prints the current medicine stock
        """
        self.intro()
        print(f"My current medicine stock is {self.medicine_stock}.")

    def heal(self, adventurer):
        """
        Heals the Adventurer.
        """
        if self.medicine_stock == 0:
            print("I'm out of medicine, sorry!")
            return

        heal_value = adventurer.max_health - adventurer.health

        if heal_value > self.medicine_stock:
            print("I can only help this much, sorry!")
            adventurer.health += self.medicine_stock
            self.medicine_stock = 0
            return

        print("Here you go, fully healed!")
        adventurer.health = adventurer.max_health
        self.medicine_stock -= heal_value

        return


healer = Healer("Bob the Healer", 80)
adventurers = ["Emma", "Peter", "Anna", "Jim", "John"]
healed_list = []

for name in adventurers:
    print()

    adventurer = Adventurer(name)
    adventurer.intro()

    if adventurer.needs_heal():
        print(f"Health of {adventurer.name} is {str(adventurer.health)}")
        healer.healer_intro()
        healer.heal(adventurer)
        print(
            f"Health of {adventurer.name} now is {str(adventurer.health)}")

    healed_list.append((adventurer.name, adventurer.health))

print(f"\n{healed_list}")
