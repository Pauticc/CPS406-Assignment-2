import A2
import pickle
from os.path import exists

login_options = ["L", "C", "Q"]
select = False
quit = False
if not exists('member_data.pkl'):
    club = A2.Club()
else:
    with open('member_data.pkl', 'rb') as inp:
        club = pickle.load(inp)

def main():
    print("Welcome to Club _______")
    global club
    global select
    global quit
    while not quit:
        while not select:
            choice = input("Enter: (L)ogin | (C)reate account | (Q)uit\n").upper()
            if choice in login_options:
                select = True
            else:
                print("Invalid input")
        if choice == "Q":
            quit_function()
        elif choice == "C":
            account_creation()
            choice == "L"
        elif choice == "L":
            while True:
                username = input("Username: ")
                password = input("Password: ")
                if check_login(username, password):
                    print("Login Successful")
                    break
                else:
                    print("You have entered an invalid username or password")
            main_Menu(username)

def main_Menu(username):
    global club
    while True:
        print("User: ", username, "Name: ", club.data[username][1], "Phone Number: ", club.data[username][2], "Paid: ", club.data[username][3], "Address: ", club.data[username][4])
        input()
    return


def check_login(username, password):
    if username in club.members and club.data[username][0] == password:
        return True
    else:
        return False

def quit_function():
    global quit
    quit = True

def account_creation():
    global club
    global select
    print("Account Creation")
    while True:
        username = input("Enter a username: ")
        if username in club.members:
            print("Username already taken")
        else:
            break
    password = input("Enter a password: ")
    name = input("Enter your name: ")
    number = input("Enter your number: ")
    address = input("Enter your address: ")
    club.add_member(username, password, name, number, False, address)
    print("Account successfully created. Redirecting to main menu...")
    with open('member_data.pkl', 'wb') as outp:
        pickle.dump(club, outp, pickle.HIGHEST_PROTOCOL)
    select = False



if __name__ == "__main__":
    main()
