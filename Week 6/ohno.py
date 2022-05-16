s1 = ["Einstein", "Curie", "Newton", "Darwin"]
s2 = ["Tesla", "Galilei", "Lovelace"]

scientist_list = s1 + s2
print("scientist_list:", scientist_list)

scientist_dict = {}

for index, scientist in enumerate(scientist_list):
    scientist_dict[scientist] = index

print("The scientist dictionary:", scientist_dict)