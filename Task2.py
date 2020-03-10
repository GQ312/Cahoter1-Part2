stud = int(input("Enter the number of students: "))
appl = int(input("Enter the number of apples: "))
"""stud_have = appl // stud
lost = appl - (stud_have * stud)
if stud > appl:
    print("Students don't have apples!")
    print(f"Apple lost {appl}")
elif stud < appl:
    print(f"Each student have {stud_have}")
    print(f"Apples lost {lost}")"""

x = appl // stud
y = appl % stud

print(x)
print(y)