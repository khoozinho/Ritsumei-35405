class Cat:
    animal_type = "carnivore"

    def __init__(self, name, color, hair, age):
        self.name = name
        self.color = color
        self.hair = hair
        self.age = age
        self.property = "cute"

    def describe(self):
        return "{} is {} years old".format(self.name, self.age)

    def say(self, sound):
        return f"{self.name} says {sound}"

class Munchkin(Cat):
    characteristic = "very short legs"

    def __init__(self, name, color, age, weight, hair="short"):
        super().__init__(name, color, hair, age)
        self.weight = weight

    def say(self ,sound="nyan"):
        return f"{self.name} says {sound}"

    def cat_info(self):
        info_dict = {
            "name": self.name,
            "color": self.color,
            "hair": self.hair,
            "age": self.age,
        }
        return info_dict

    def another_describe(self):
        return super().describe() + " and " + self.color

oliver = Munchkin("Oliver", "black", 1, 2.4)
print(oliver.name + "'s hair is" + oliver.hair)

loki = Munchkin("Loki", "black", 7, 4.2, "long")
print(loki.name + "'s hair is" + loki.hair)
print(loki.describe())
print(loki.another_describe())