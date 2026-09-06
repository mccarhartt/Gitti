luku = int(input("Luku : "))
for luku1 in range(2,luku):
    if luku % luku1 ==0:
        print("alkuluku")
    else:
        print("ei ole alkuluku")
        break