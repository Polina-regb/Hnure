class BankAccount:
    def __init__(self, owner):
        self.owner = owner
        self.balance = 0

    def deposit(self, amount):
        self.balance += amount
        print("Баланс пополнен на {amount}")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print("Снято {amount}")
        else:
            print("Недостаточно средств")

    def show_balance(self):
        print("Владелец:", self.owner)
        print("Баланс:", self.balance)


name = input("Введите имя владельца: ")
account = BankAccount(name)

while True:
    print("Что вы хотите сделать?")
    print("1 - Пополнить")
    print("2 - Снять")
    print("0 - нечего")

    choice = input("Ваш выбор: ")

    if choice == "1":
        amount = int(input("Введите сумму: "))
        account.deposit(amount)

    elif choice == "2":
        amount = int(input("Введите сумму: "))
        account.withdraw(amount)

    elif choice == "0":
        break
