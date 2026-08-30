#A on ikkunallinen hytti autokannen yläpuolella.
#B on ikkunaton hytti autokannen yläpuolella.
#C on ikkunaton hytti autokannen alapuolella.
#Jos käyttäjä syöttää kelvottoman hyttiluokan, ohjelma tulostaa Virheellinen hyttiluokka.
hyttiluoka = input("hyttiluoka: ")
if hyttiluoka == "LUX":
    print("LUX on parvekkeellinen hytti yläkannella.")
elif hyttiluoka == "A":
    print("A on ikkunallinen hytti autokannen yläpuolella.")
elif hyttiluoka == "B":
    print("B on ikkunaton hytti autokannen yläpuolella.")
elif hyttiluoka == "C":
    print("C on ikkunaton hytti autokannen alapuolella.")
else:
    print("Virheellinen hyttiluokka.")