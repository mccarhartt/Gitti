cities = []
city = input("kaupungin nimi : ")
maara = 0
while maara < 5:
    cities.append(city)
    city = input("kaupungin nimi : ")
    maara += 1

for city in cities[:6]:
    print(city)