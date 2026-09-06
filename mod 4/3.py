#Kirjoita ohjelma, joka kysyy käyttäjän biologisen sukupuolen ja hemoglobiiniarvon (g/l). Ohjelma ilmoittaa, onko hemoglobiiniarvo alhainen, normaali vai korkea.
#Naisen normaali hemoglobiiniarvo on välillä 117-175 g/l.
#Miehen normaali hemoglobiiniarvo on välillä 134-195 g/l.
sukupuoli = input("sukupuoli: ")
arvo = int(input("hemoglobiiniarvo: "))
if sukupuoli =="nainen":
    if 117>arvo or 175<arvo:
        print("hemoglobiiniarvo ei ole normaali")
    else:
        print("hemoglobiiniarvo on normaali")
elif sukupuoli =="mies":
    if 134>arvo or 195<arvo:
        print("hemoglobiiniarvo ei ole normaali")
    else:
        print("hemoglobiiniarvo on normaali")