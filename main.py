import A2
import pickle
from os.path import exists

login_options = ["L", "C", "Q"]
treasurer_menu = ["F", "C", "Q", "S"]
coach_menu = ["M", "Q"]
member_menu = ["P", "Q"]
treasurer_string = "abcdefg"
coach_string = "123456"
choice = "none"
acc_Index = 6
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
            if club.data[username][acc_Index] == "M":
                main_Menu_Member(username)
            elif club.data[username][acc_Index] == "C":
                main_Menu_Coach(username)
            else:
                main_Menu_Treasurer(username)

def reset_select():
    global select
    select = False

def main_Menu_Member(username):
    global club
    while True:
        print("------------------Member Account------------------")
        print("Username: ", username, "Name: ", club.data[username][1], "Phone Number: ", club.data[username][2], "Address: ", club.data[username][4])
        print("Paid: ", club.data[username][3],)
        while True:
            choice = input("Enter: (P)ayment | (Q)uit\n").upper()
            if choice in member_menu:
                break
            else:
                print("Invalid input")
        if choice == "Q":
            break
        else:
            if choice == "P":
                print("Some Pay code")
        
    reset_select()
def main_Menu_Coach(username):
    global club
    while True:
        print("------------------Coach Account------------------")
        print("Username: ", username, "Name: ", club.data[username][1], "Phone Number: ", club.data[username][2], "Address: ", club.data[username][4])
        print("List of Members: ", club.members)
        while True:
            choice = input("Enter: (M)ember Management | (Q)uit\n").upper()
            if choice in coach_menu:
                break
            else:
                print("Invalid input")
        if choice == "Q":
            break
        else:
            if choice == "M":
                print("List of Members: ")
                print(club.members)
                while True:
                    M_management = input("Enter: (R)emove Member | (Q)uit\n").upper()
                    if M_management in ["R", "Q"]:
                        break
                    else:
                        print("Invalid input")
                if M_management == "R":
                    while True:
                        member_R = input("Enter the Username of the Member to Remove: ")
                        if member_R in club.members:
                            club.remove_member(member_R)
                            print("Successfully removed", member_R)
                            break
                        else:
                            print("Invalid Input")
    reset_select()

def main_Menu_Treasurer(username):
    global club
    quit = False
    while not quit:
        print("------------------Treasurer Account------------------")
        print("Username:", username, "Name:", club.data[username][1])
        print("Revenue: $", club.revenue, "Cost: $", club.cost, "Profit: $", club.profit)
        print("Current month's account payables: ")
        print("Log of Unpaid Debt from Previous Months: ")
        while True:
            choice = input("Enter: (F)inances | (C)oach Management | (S)chedule | (Q)uit\n").upper()
            if choice in treasurer_menu:
                break
            else:
                print("Invalid input")
        if choice == "Q":
            quit = True
        else:
            if choice == "F":
                revenue = input("Enter credits: $")
                expenses = input("Enter expenses: $")
                club.add_revenue(float(revenue))
                club.add_expense(float(expenses))
                club.log_profit()
                club.display_profit()
            elif choice == "C":
                print("List of Coaches: ")
                print(club.coaches)
                while True:
                    C_management = input("Enter: (R)emove Coach | (Q)uit\n").upper()
                    if C_management in ["R", "Q"]:
                        break
                    else:
                        print("Invalid input")
                if C_management == "R":
                    while True:
                        coach_R = input("Enter the Username of the Coach to Remove: ")
                        if coach_R in club.coaches:
                            club.remove_coach(coach_R)
                            print("Successfully removed", coach_R)
                            break
                        else:
                            print("Invalid Input")
            elif choice == "S":
                print("Some Schedule Code")
    save_object()
    reset_select()




def check_login(username, password):
    if username in club.data and club.data[username][0] == password:
        return True
    else:
        return False

def quit_function():
    global quit
    quit = True
    save_object()

def save_object():
    global club
    with open('member_data.pkl', 'wb') as outp:
        pickle.dump(club, outp, pickle.HIGHEST_PROTOCOL)

def account_creation():
    global club
    global select
    print("Account Creation")
    while True:
        print("Enter: (M)ember Account | (S)pecial Account")
        account_T = input().upper()
        if account_T in ["M", "S"]:
            break
        else:
            print("Invalid Input")
    if account_T == "M":
        print("Member Account Creation")
    else:
        while True:
            special_str = input("Enter the Special Code: ")
            if special_str != treasurer_string and special_str != coach_string:
                print("Invalid Code")
            else:
                break
        if special_str == coach_string:
            print("Coach Account Creation")
        else:
            print("Treasurer Account Creation")
    while True:
        username = input("Enter a username: ")
        if username in club.data:
            print("Username already taken")
        else:
            break
    password = input("Enter a password: ")
    name = input("Enter your name: ")
    number = input("Enter your number: ")
    address = input("Enter your address: ")
    if account_T == "M":
        club.add_member(username, password, name, number, False, address)
    else:
        if special_str == coach_string:
            club.add_coach(username, password, name, number, address)
        else:
            club.add_Treasuer(username, password, name, number, address)
    print("Account successfully created. Redirecting to main menu...")
    save_object()
    reset_select()
    

if __name__ == "__main__":
    main()
