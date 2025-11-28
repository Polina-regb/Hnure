def плюс(a,b):
    return a + b
def минус(a,b):
    return a-b
def умножить(a,b):
    return a*b
def разделить(a,b):
    return a/b



def calculate(a, b, oper):
    if oper == '+':
        return плюс(a, b)
    elif oper == '-':
        return минус(a, b)
    elif oper == '*':
        return умножить(a, b)
    elif oper == '/':
        if b == 0:
            return "Помилка"
        return разделить(a, b)
    else:
        return "Помилка"

cont = "так"

while cont.lower() == "так":
    a = float(input("Введіть перше число: "))
    b = float(input("Введіть друге число: "))
    oper = input("Введіть знак (+, -, *, /): ")

    print("Результат:", calculate(a, b, oper))

    cont = input("Продовжити? (так/ні): ")