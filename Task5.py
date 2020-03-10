class1 = int(input("Students in class #1: "))
class2 = int(input("Students in class #2: "))
class3 = int(input("Students in class #3: "))
"""if class1 % 2 == 0:
    print("Class #1 needs " + str(int(class1 / 2)))
else:
    print("Class #1 needs " + str(int((class1 / 2) + 1)))
if class2 % 2 == 0:
    print("Class #1 needs " + str(int(class2 / 2)))
else:
    print("Class #1 needs " + str(int((class2 / 2)) + 1))
if class3 % 2 == 0:
    print("Class #1 needs " + str(int(class3 / 2)))
else:
    print("Class #1 needs " + str(int((class3 / 2)) + 1))"""

class1 = class1 // 2 + class1 % 2
class2 = class2 // 2 + class2 % 2
class3 = class3 // 2 + class3 % 2
print(f"Class #1 needs {class1} desks.")
print(f"Class #2 needs {class2} desks.")
print(f"Class #3 needs {class3} desks.")
print(f"Total {class1 + class2 + class3} desks.")