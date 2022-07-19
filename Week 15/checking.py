#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul 15 11:06:36 2022

@author: lisa
W15
"""

# class Cat:
#     animal_type = "carnivore"
    
#     def __init__(self, name, color, hair, age):
#         self.name = name
#         self.color = color
#         self.hair = hair
#         self.age = age
        
#     def say(self, sound):
#         return"{} says {}".format(self.name, sound)
        
# class Persian(Cat):
#     pass

# class Siamese(Cat):
#     pass

# class Munchkin(Cat):
#     pass

# luna = Persian("Luna", "white", "long", 2)
# milo = Siamese("Milo", "gray", "short", 4)
# oliver = Munchkin("Oliver", "black", "short", 1)


# cats = [luna, milo, oliver]
# for cat in cats:
#     print(cat.name, "is", cat.color+",", cat.hair, "haired", "abd", cat.age, "years old.")
#     if cat.name == "Luna":
#         print(cat.say("meow"))
#     else:
#         print(cat.say("nyan"))


# class Cat:
#     animal_type = "carnivore"
    
#     def __init__(self, name, color, hair, age):
#         self.name = name
#         self.color = color
#         self.hair = hair
#         self.age = age
        
#     def say(self, sound):
#         return"{} says {}".format(self.name, sound)


# class Persian(Cat):
#     def say(self, sound="meow"):
#         return "{} says {}".format(self.name, sound)

# class Siamese(Cat):
#     def say(self, sound="nyan"):
#         return "{} says {}".format(self.name, sound)

# class Munchkin(Cat):
#     def say(self, sound="nyan"):
#         return "{} says {}".format(self.name, sound)


# luna = Persian("Luna", "white", "long", 2)
# milo = Siamese("Milo", "gray", "short", 4)
# oliver = Munchkin("Oliver", "black", "short", 1)

# print(luna.say())
# print(milo.say())
# print(oliver.say())

# print(oliver.say("nyaaan"))


#2
class Cat:
    """
    """
    animal_type = "carnivore"
    
    def __init__(self, name, color, hair, age):
        self.name = name
        self.color = color
        self.hair = hair
        self.age = age
        
        self.property = "cute"
    
    def describe(self):
        """
        """
        return"{} is {} years old".format(self.name, self.age)
        
    def say(self, sound):
        return "{} says {}".format(self.name, sound)

class Munchkin(Cat):
    characteristic = "very short legs"
    
    def __init__(self, name, color, age, weight, hair="short"):
        super().__init__(name, color, hair, age)
        self.weight = weight
    
    def say(self, sound="nyan"):
        return f"{self.name} says {sound}"

    def cat_info(self):
        info_dict = {
            "name":self.name, 
            "color":self.color,
            "age":self.age, 
            "hair":self.hair
            }
        return info_dict
    
    def another_describe(self):
        return super().describe() + " and " + self.color


oliver = Munchkin("Oliver", "black", 1, 2.4)
print(oliver.name + "'s hair is" + oliver.hair)
loki = Munchkin("Loki", "black", 7, 4.2, "long")
print(loki.name, "'s hair is", loki.hair)
print(loki.describe())
print(loki.another_describe())
print(loki.name, "is", loki.animal_type, "but has", loki.characteristic)
print(loki.name, "is", loki.property)
loki.property = "very cute"
print(loki.name, "is", loki.property)
loki_dict = loki.cat_info()
print("Dictionary about Loki:", loki_dict)
print("Type of the object loki:", type(loki))
print("Is loki an instance of Munchkin?")
print(isinstance(loki, Munchkin))
print("Is loki an instance of Cat?")
print(isinstance(loki, Cat))