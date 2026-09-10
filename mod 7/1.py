import random
def luku():
    luku = random.randint(1, 6)
    return luku
while True:
    luku1 = luku()
    print(luku1)
    if luku1 == 6:
        break