import os
import sqlite3
from subprocess import call
from time import sleep

class User:
    def __init__(self, name, phone_number, address):
        self.name = name
        self.phone_number = phone_number
        self.address = address

class Performance:
    def __init__(self, name, performance, area):
        self.name = name
        self.performance = performance
        self.area = area

# Clear terminal
def clear():
    _ = call('clear' if os.name == 'posix' else 'cls')

# Exit program
def exit():
    clear()
    print("\n Avslutter program...")
    
def auth_login():
    print("LOGIN TODO")
    # Check DB for user
    # Return user
    current_user = User("Vetle", "+471234", "Sandkollveien 22")
    return current_user

def auth_register():
    print("REGISTER TODO")
    # Check DB for user
    # If user does not exist register, cont.
    # If not retry
    # return user



def login():
    while True:
        try:
            print("Hva ønsker du å gjøre?")
            print('1. Logg inn \n2. Registrere ny bruker\n3. Avslutt\n')
            main_menu = int(input("Skriv inn tall: "))
            
            if main_menu == 1:
                return 1
            elif main_menu == 2:
                return 2
            elif main_menu == 3:
                exit()
                break
            else:
                clear()
                print("\n \n** " + str(main_menu) + " er en ukjent kommando **\n")

        except ValueError:
            print("\nFeil input, bruk tall!\n")

def buy_ticket():
    print("Ticket TODO")

def choose_ticket_area():
    while True:
            try:
                clear()
                print("Velg Sitteområde:\n")
                print("1. Parkett")
                print("2. Balkong")
                print("3. Galleri \n")
                print("4. Avslutt")

                area = int(input("Skriv inn tall: "))

                if area > 0 and area < 4:
                    return area
                elif area == 4:
                    exit()
                    break
                else:
                    clear()
                    print("\n \n** " + str(area) + " er en ukjent kommando **\n")
            
            except ValueError:
                print("\nFeil input, bruk tall!\n")

def choose_seat(seating_area):
    capacity = 0

    if seating_area == 0:
        # Kongsemnene Hovedscene todo: missing seat numbers
        print("TODO")
    elif seating_area == 1:
        print("TODO")
    elif seating_area == 2:
        print("TODO")
    elif seating_area == 3:
        print("TODO")

def select_performance(current_user):
    while True:
        try:
            print("\nHei, "+current_user.name +"\nVelg forestilling!\n----------------------------")
            print('1. Kongsemnene \n2. Størst av alt er kjærligheten\n3. Avslutt\n')

            viewing = int(input("Skriv inn tall: "))

            if viewing == 1:
                while True:
                    try:
                        clear()
                        print("Visninger av Kongsemnene:\n")
                        print("1. 1.feb")
                        print("2. 2.feb")
                        print("3. 3.feb")
                        print("5. 5.feb")
                        print("6. 6.feb \n")
                        print("7. Avslutt")

                        theater_viewing = int(input("Skriv inn tall: "))

                        if theater_viewing > 0 and theater_viewing < 7:
                            chosen_performance = Performance("Kongsemnene", theater_viewing, 0)
                            return chosen_performance
                        elif theater_viewing == 7:
                            exit()
                            break
                        else:
                            clear()
                            print("\n \n** " + str(theater_viewing) + " er en ukjent kommando **\n")
                    
                    except ValueError:
                        print("\nFeil input, bruk tall!\n")
            elif viewing == 2:
                    while True:
                        try:
                            clear()
                            print("Visninger av Størst av alt er kjærligheten:\n")
                            print("1. 3.feb")
                            print("2. 6.feb")
                            print("3. 7.feb")
                            print("5. 12.feb")
                            print("6. 13.feb")
                            print("7. 14.feb\n")
                            print("8. Avslutt")

                            theater_viewing = int(input("Skriv inn tall: "))

                            if theater_viewing > 0 and theater_viewing < 8:
                                area = choose_ticket_area()
                                chosen_performance = Performance("Kongsemnene", theater_viewing, area)
                                return chosen_performance
                            elif theater_viewing == 8:
                                exit()
                                break
                            else:
                                clear()
                                print("\n \n** " + str(theater_viewing) + " er en ukjent kommando **\n")
                        
                        except ValueError:
                            print("\nFeil input, bruk tall!\n")
            else:
                clear()
                print("\n \n** " + str(area) + " er en ukjent kommando **\n")

        except ValueError:
            print("\nFeil input, bruk tall!\n")

def main():
    print("\nVelkommen til teaterbestilling!\n----------------------------")
    login_choice = login()
    
    if login_choice == 1:
        clear()
        current_user = auth_login()
        current_performance = select_performance(current_user)

    elif login_choice == 2:
        clear()
        main()

main()