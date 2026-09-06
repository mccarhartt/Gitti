import random
luku = random.randint(1,10)
while True:
    luku1 = int(input("luku : "))
    if luku1 < luku:
        print("Liian pieni")
    elif luku1 > luku:
        print("Liian suuri")
    else:
        print("Oikein")
        break

