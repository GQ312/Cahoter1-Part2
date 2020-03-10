num = int(input("Write your number: "))
for i in range(1, num + 1):
    i = i ** 2
    if i <= num:
        print(i)