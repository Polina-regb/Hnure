Km = int(input("відстань до міста(km) "))
vid = int(input("середня швідкість автомабіля(km/god) "))
many = int(input("вартість одного літра бензину (у грн) "))
whave = int(input("скільки літрів бензину авто споживає на 100 км "))

itog_god = round((Km / vid))
benz = round((Km * whave / 100))
groshi = round((benz * many))

print("Це вся інформація, яка вам потрібна:")
print(f"Час у дорозі: {itog_god}")
print(f"Витрати бензину: {benz}")
print(f"Вартість поїздки: {groshi}")
