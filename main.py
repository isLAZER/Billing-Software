# Importing modules
from modules.login import *
from modules.billing import *
from modules.stocks import *
from modules.settings import *
from modules.Info_doc import Info_display
from modules.register import *


<<<<<<< HEAD
=======
# current date
now = datetime.now()
today = date.today()
print("Today's date:", today)
print()

>>>>>>> 83cc5ee37429151d7708157b98dbabe4bf0cd010
print("Login:")
username_in = input("Enter your username: ")
password_in = input("Enter your password: ")
# Login
user = login(username_in, password_in)

# Menu
# admin/owner menu
if user == "ADMIN":
    while True:
        c = int(input("\nMenu:-\n(1) Item Shop\n(2) Stocks\n(3) Register\n(4) Shop details\n(5) Settings\n(6) Show Calender \n(7) Log Out\n..> "))
        if c == 1:
            shop()
        elif c == 2:
            stocks()
        elif c == 3:
            register()
        elif c == 4:
            Info_display()
        elif c == 5:
            setting()
<<<<<<< HEAD
        elif c==6:
            showcalendar()
        elif c==7:
=======
        elif c == 6:
            print()
            print(now.strftime("date: %d/%m/%Y\ntime: %H:%M"))
            print()
            print(cal())
            print()
        elif c == 7:
>>>>>>> 83cc5ee37429151d7708157b98dbabe4bf0cd010
            break
        else:
            print("OPTION NOT AVAILABLE ")

# customer menu
else:
<<<<<<< HEAD
    while True:        
        c = int(input("\nMenu:-\n(1) Item Shop \n(2) My Cart\n(3) Show Calendar\n(4) Log Out \n..> "))
        if c==1:
=======
    while True:
        c = int(input(
            "\nMenu:-\n(1) Item Shop \n(2) My Cart\n(3) Show Calender\n(4) Log Out \n..> "))
        if c == 1:
>>>>>>> 83cc5ee37429151d7708157b98dbabe4bf0cd010
            item_shop()
        elif c == 2:
            a = billing()
            checkout(a)
            break
<<<<<<< HEAD
        elif c==3:
            showcalendar()
        elif c==4:
=======
        elif c == 3:
            print()
            print(now.strftime("date: %d/%m/%Y\ntime: %H:%M"))
            print()
            print(cal())
            print()
        elif c == 4:
>>>>>>> 83cc5ee37429151d7708157b98dbabe4bf0cd010
            break
        else:
            print("OPTION NOT AVAILABLE ")

# good bye
print("\nTHANK YOU FOR USING OUR SOFTWARE...\nHAVE A NICE DAY! :)\n ")
print()
<<<<<<< HEAD
ex=input("stratagic halt~")   
=======
ex = input("SS taken?")
>>>>>>> 83cc5ee37429151d7708157b98dbabe4bf0cd010
