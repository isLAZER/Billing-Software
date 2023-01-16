# Importing modules
from modules.Info_doc import Info_input
import pickle
import calendar
from datetime import *

# current date
now = datetime.now()
today = date.today()
print("Today's date:", today)
print()

# finds current mounth calender


def cal():
    today = date.today()
    mth = today.month
    yr = today.year
    cal = calendar.month(yr, mth)
    return cal

# display calendar


def showcalendar():
    print()
    print('--------------------')
    print(now.strftime("date: %d/%m/%Y\ntime: %H:%M"))
    print()
    print(cal())
    print('--------------------')
    print()


# settings menu
def setting():
    while True:
        c = input(
            '\nSettings:-\n(1) Change admin username and password\n(2) Change shop details\n\n[Press X to exit]\n..> ')
        # administrator settings
        if c == '1':
            a = input(
                "  Do you really want to change administrator settings?\n(They are very impotant for your software to work properly)\n[Press Y to confirm!]\n..> ")
            if a == 'y' or a == 'Y':
                file = open("Backend/admin.dat", "wb")
                username = str(input("Enter the new ADMIN username: "))
                while True:
                    password = str(input("Enter new ADMIN password: "))
                    rec = {'user': username, 'pass': password}
                    confirm_pass = str(input("Confirm password : "))
                    if password == confirm_pass:
                        pickle.dump(rec, file)
                        print('Setup complete!\nUsername and Password changed...')
                        break
                    else:
                        print("Error!\n---Please Retry!")
                        continue
                print()
                file.close()
            else:
                break

        # shop settings
        elif c == '2':
            print("Continue with changing shop details?")
            z = input(
                "[the previous data will be lost forever]\nPress 'Y' to Confirm\n..> ")
            if z == 'y' or z == 'Y':
                Info_input()
                break
            else:
                print("exit!")
                break
        elif c == 'x' or c == 'X':
            break
        else:
            break
