def f(halkaisija, hinta):
    pinta = 3.14 * halkaisija/2/100 *halkaisija/2/100
    yksikkohinta = hinta/pinta
    return yksikkohinta
halkaisija1 = int(input("halkaisija1: "))
hinta1 = int(input("hinta1: "))
halkaisija2 = int(input("halkaisija2: "))
hinta2 = int(input("hinta2: "))
yksikkohinta1 = f(halkaisija1, hinta1)
yksikkohinta2 = f(halkaisija2, hinta2)
if yksikkohinta1 < yksikkohinta2:
    print("Ensimmäinen pizza.")
elif yksikkohinta2 < yksikkohinta1:
    print("Toinen pizza.")
else:
    print("Pizzat ovat sama.")