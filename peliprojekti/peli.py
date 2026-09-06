#Tee kansioon ohjelma, joka kysyy pelaajan nimen ja iän, tallentaa nämä muuttujiin ja tulostaa konsoliin.
nimi=input("Sinun nimi: \n")
ika=int(input("Sinun ikä: \n"))

if ika < 12:
    print("Olet liian nuori")
else:
    print("Tervetuloa!")

    while True:
        print("PÄÄVALIKKO")
        print("1")
        print("2")
        print("3")
        print("lopeta")

        komento = input("komento : ")

        if komento == "1":
            print("start")
        elif komento == "2":
            print("pause")
        elif komento == "3":
            print("asetukset")
        elif komento == "lopeta":
            print("Lopetetaan")
            break


