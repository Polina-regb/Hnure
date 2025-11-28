def to_seconds(hours):
    return hours * 3600

hours = float(input("Введіть кількість годин: "))
seconds = to_seconds(hours)
print("стільки вийшло:", seconds,)
