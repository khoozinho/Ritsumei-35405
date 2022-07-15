class Cat:
    animal_type = "carnivore"

    def __init__(self, name, color, hair, age):
        self.name = name
        self.color = color
        self.hair = hair
        self.age = age

    def say(self, sound):
        return f"{self.name} says {sound}"

class Persian(Cat):
    def say(self, sound="meow"):
        return f"{self.name} says {sound}"

class Siamese(Cat):
    def say(self, sound="nyan"):
        return f"{self.name} says {sound}"

class Munchkin(Cat):
    def say(self, sound="nyan"):
        return f"{self.name} says {sound}"

luna = Persian("Luna", "white", "long", 2)
milo = Siamese("Milo", "gray", "short", 4)
oliver = Munchkin("Oliver", "black", "short", 1)

print(luna.say())
print(milo.say())
print(oliver.say())

print(oliver.say("nyaaan"))

