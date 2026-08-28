lager = {
    "Apfel": 3,
    "Milch": 1
}

produkte = "Mandeln"
menge = 4

lager[produkte] = lager.get(produkte, 0) + menge 

print(lager)

for produkte, menge in lager.items():
    print(f"{produkte}: {menge}")

    