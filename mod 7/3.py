def bensiini(gallona):
    litra = gallona * 3.785
    return litra
while True:
    gallonat = float(input("määrä: "))
    if gallonat < 0:
        break
    litrat = bensiini(gallonat)
    print(litrat)