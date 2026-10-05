class Pelaaja:

    def __init__(self, nimi, sijainti):
        self.nimi = nimi
        self.sijainti = sijainti
        self.esineet = []

#With this method you can change location
    def change_room(self, next_room):
        self.sijainti = next_room
        print(f"\n You have been moved to the {next_room.nimi}")

#With this method you can take items and add them to inventory
    def take_item(self):

        if self.sijainti.esine:
            esine = self.sijainti.esine
            self.esineet.append(esine)
            self.sijainti.esine = None
            print(f"You took {esine.nimi}")

        else:
            print("There is nothing in the room")

#With this method you can check items in your inventory
    def check_inventory(self):
        print("\n == INVENTORY ==")

        if not self.esineet:
            print("Your inventory is empty")
        else:
            for esine in self.esineet:
                print(f"{esine}")

class Huone:

    def __init__(self, nimi, esine):
        self.nimi = nimi
        self.esine = esine

#Show players current location
    def current_location(self):
        print(f"\nYou are now in the {self.nimi}")

        if self.esine:
            print(f"There is {self.esine} in this room")

        else:
            print("The room is empty")

class Esine:

    def __init__(self, nimi, vari):
        self.nimi = nimi
        self.vari = vari

    def __str__(self):
        return f"{self.vari} {self.nimi}"

#Intro and instructions

def intro():
    with open("intro.txt", "r") as tiedosto:
        return tiedosto.read()

def ohjeet():
    with open("ohjeet.txt", "r") as tiedosto:
        return tiedosto.read()

#saving
    
def save_game(pelaaja, huoneet):

    with open("saving.txt", "w") as tiedosto:

#save player's name
        tiedosto.write(pelaaja.nimi)                  

#save player's location
        tiedosto.write("\n" + pelaaja.sijainti.nimi)   

#save items in player's inventory
        for esine in pelaaja.esineet:
            tiedosto.write("\n" +esine.nimi)

    print("Succeessful save!")

#loading game

def load_game(pelaaja, huoneet, kaikki_esineet):

    try:
        with open("saving.txt", "r") as tiedosto:
#load player*s name
            nimi = tiedosto.readline()[:-1]
#load player*s location
            sijainti = tiedosto.readline()[:-1]

            if nimi != pelaaja.nimi:
                return False

            for huone in huoneet:
                if huone.nimi == sijainti:
                    pelaaja.sijainti = huone

            pelaaja.esineet =[]

            while True:
                rivi = tiedosto.readline()

                if rivi == "":
                    break

#load player*s inventory
                for esine in kaikki_esineet:
                    if rivi ==esine.nimi:
                        pelaaja.esineet.append(esine)

#delete items, which player already took from the room
                        for huone in huoneet:
                            if huone.esine == esine:
                                huone.esine = None
            

            print("Game have been loaded!")
            return True
    except:
        return False

#all items

basketball = Esine("basketball", "orange")
soccer_ball = Esine("soccer ball", "white")
volleyball = Esine("volleyball", "yellow")

kaikki_esineet = [basketball, soccer_ball, volleyball]

#all locations

basketball_court = Huone("basketball court", basketball)
football_field = Huone("football field", soccer_ball)
volleyball_court = Huone("volleyball court", volleyball)

kaikki_huoneet = [basketball_court, football_field, volleyball_court]

#start game

print(intro())

nimi = input("Your name: ")
ika = int(input("Your age: "))

#age checking

if ika < 12:
    print("You are too young(")

else:

    #loading game
    pelaaja = Pelaaja(nimi, basketball_court)

    if load_game(pelaaja, kaikki_huoneet, kaikki_esineet):
        print(f"Welcome back!")

    else:
        print(f"Welcome to the new game!")

#main menu 
    while True:
        print("\n=== MAIN MENU ===")

        print(f"Your current location is {pelaaja.sijainti.nimi}")

        print("1. Current room")
        print("2. Take item")
        print("3. Check inventory")
        print("4. Change room")
        print("5. Save game")
        print("6. View instructions")
        print("end - Save game and quit")

        komento = input("Choose the action: ")

        if komento == "1":

            pelaaja.sijainti.current_location()

        elif komento == "2":

            pelaaja.take_item()

        elif komento == "3":

            pelaaja.check_inventory()

        elif komento == "4":

            print("\nWhere you want to move?")

            print("1. Basketball court")
            print("2. Football field")
            print("3. Volleyball court")

            kohde = input("Choose the room: ")

            if kohde == "1":
                pelaaja.change_room(basketball_court)
            elif kohde == "2":
                pelaaja.change_room(football_field)
            elif kohde == "3":
                pelaaja.change_room(volleyball_court)

        elif komento == "5":

            save_game(pelaaja, kaikki_huoneet)

        elif komento == "6":
            print(ohjeet())

        elif komento == "end":
            save_game(pelaaja, kaikki_huoneet)
            print("Thank you for game!")
            print("See you next time!")
            break

        else:
            print("Unknown command")


