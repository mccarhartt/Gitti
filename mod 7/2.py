import random
noppa = int(input("noppa: "))
def luku(noppa):
    luku = random.randint(1, noppa)
    return luku
while True:
    luku1 = luku(noppa)
    print(luku1)
    if luku1 == noppa:
        break