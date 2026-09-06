luku = int(input("luku : \n"))
pienin = 10000000000
suurin = 0
while luku != " ":
    print(luku)
    if luku < pienin:
        pienin == luku
    elif luku<suurin:
        suurin == luku
    break
print(pienin)
print(suurin)
