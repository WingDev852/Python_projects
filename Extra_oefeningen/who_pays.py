import random
names = input("Geef namen, gescheiden door komma's: ").split(",")
payer = random.choice(names)
print(f"{payer} betaalt vandaag!")
