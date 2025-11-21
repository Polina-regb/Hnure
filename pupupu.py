N = int(input("Введіть число N: "))

print("Парні числа від 1 до", N, ":")

for i in range(1, N):
    if i % 2 == 0:
        print(i)