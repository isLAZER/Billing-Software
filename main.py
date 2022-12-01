#Importing modules
from modules.login import *
from modules.billing import *
from modules.stocks import *
from modules.settings import *

username_in = input("Enter your username: ")
password_in = input("Enter your password: ")

user=login(username_in,password_in)

if user=="ADMIN":
    while True:
        c = int(input("\n(1) Item Shop\n(2) Stocks\n(3) Cash Register\n(4) Shop details\n(5) Settings\n..> "))    
        if c==1:
            shop()
            break
        elif c==2:
            stocks()
            break
        elif c==3:
            #cash register in work!
            break
        elif c==4:
            #shop details page in working!
            break
        elif c==5:
            #settings in work!
            break
        else:
            print("OPTION NOT AVAILABLE ")

else:
    while True:        
        c = int(input("\n(1) Item Shop \n(2) Billing \n(3) Log Out \n..> "))
        if c==1:
            item_shop()
        elif c==2:
            billing()
            break
        elif c==3:
            break
        else:
            print("OPTION NOT AVAILABLE ")        
    

print("THANK YOU FOR USING OUR SOFTWARE...\nHAVE A NICE DAY! :) ")   
