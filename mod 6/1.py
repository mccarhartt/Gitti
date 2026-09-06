import random
maara = int(input("määrä : \n"))
sum = 0
for n in range(maara):
    luku = random.randint(1,6)
    sum += luku
print(sum)
