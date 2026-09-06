nimi = "python"
sala = "rules"
while True:
    nimi1 = input("Nimi : ")
    sala1 = input("Salasana : ")
    if nimi1 != nimi or sala1 != sala:
        print("Pääsy evätty")
    else:
        print("Tervetuloa")
    break
