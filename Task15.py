ages = int(input("Write your ages: "))
if ages % 2 == 1:
    for i in range(1, ages + 1, 2):
        print(i)
else:
    for i in range(2, ages + 1, 2):
        print(i)