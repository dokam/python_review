cars = ["Ford", "Volvo", "BMW"]


cars.append("Honda")
print(len(cars))

cars.pop(1)
cars.remove("BMW")

cars.reverse()
cars.sort()

for x in cars:
    print(x.upper())

print(cars.count('Ford'))