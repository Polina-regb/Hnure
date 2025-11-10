a = float(input("Введіть перше число: "))
b = float(input("Введіть друге число: "))
oper = input("Введіть знак (+, -, *, /): ")

if oper == '+':
    print(f"Результат: {a + b}")
elif oper == '-':
    print(f"Результат: {a - b}")
elif oper == '*':
    print(f"Результат: {a * b}")
elif oper == '/':
    if b != 0:
        print(f"Результат: {a / b}")
    else:
        print("Помилка")
else:

    print("Помилка")
