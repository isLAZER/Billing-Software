#Importing modules
from modules.login import *
from modules.billing import *
from modules.stocks import *
from modules.settings import *
from modules.Info_doc import Information
from modules.register import *
from datetime import *


#current date
today = date.today()
print("Today's date:", today)
print()

print("Login:")
username_in = input("Enter your username: ")
password_in = input("Enter your password: ")
#Login 
user=login(username_in,password_in)

#Menu 
#admin/owner menu
if user=="ADMIN":
    while True:
        c = int(input("\nMenu:-\n(1) Item Shop\n(2) Stocks\n(3) Register\n(4) Shop details\n(5) Settings\n(6) Log Out\n..> "))    
        if c==1:
            shop()
        elif c==2:
            stocks()
        elif c==3:
            register()
        elif c==4:
            Information()
        elif c==5:
            setting()
        elif c==6:
            break
        else:
            print("OPTION NOT AVAILABLE ")

#customer menu
else:
    while True:        
        c = int(input("\nMenu:-\n(1) Item Shop \n(2) My Account \n(3) Log Out \n..> "))
        if c==1:
            item_shop()
        elif c==2:
            a=billing()
            checkout(a)
            break
        elif c==3:
            break
        else:
            print("OPTION NOT AVAILABLE ")        
    
#good bye
print("THANK YOU FOR USING OUR SOFTWARE...\nHAVE A NICE DAY! :) ")   
