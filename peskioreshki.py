Km = int (input("відстань до міста(km) "))
vid = int (input("середня швідкість автомабіля(km/god) "))
many = int (input("вартість одного літра бензину (у грн) "))
whave = int (input("скільки літрів бензину авто споживає на 100 км "))

itog_god = (Km / vid)
benz = Km * whave / 100
groshi = (benz * many)

print("Це вся інформація, яка вам потрібна:")
print("Час у дорозі:", round(itog_god))
print("Витрати бензину:", round(benz))
print("Вартість поїздки:", round(groshi))