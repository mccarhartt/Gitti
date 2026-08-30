#Kirjoita ohjelma, joka arpoo ja tulostaa kaksi erilaista numerolukon koodia:
#kolmenumeroisen koodin, jonka kukin numeromerkki on väliltä 0..9.
#nelinumeroisen koodin, jonka kukin numeromerkki on väliltä 1..6.
import random
luku1=random.randint(0,9)
luku2=random.randint(0,9)
luku3=random.randint(0,9)
luku4=random.randint(1,6)
luku5=random.randint(1,6)
luku6=random.randint(1,6)
luku7=random.randint(1,6)
print(f"{luku1}{luku2}{luku3}")
print(f"{luku4}{luku5}{luku6}{luku7}")