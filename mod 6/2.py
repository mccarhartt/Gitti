luvut = []
luku = input("luku : ")
while luku != " ":
    luvut.append(luku)
    luku = input("seurava luku : ")
luvut.sort(reverse=True)
for luku in luvut[:5]:
    print(luku)
