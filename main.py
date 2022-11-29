#Importing modules
from modules.login import *
from modules.billing import *
from modules.stocks import *
from modules.settings import *
from modules.calculator import calculator

username_in = input("Enter your username: ")
password_in = input("Enter your password: ")

user=login(username_in,password_in)

if user=="ADMIN":  
    while True:
        c = int(input("\n (1) Stocks\n (2) Calculator\n (3) Shop details\n>>>"))    
        if c==1:
            stocks()
            break
        elif c==2:
            calculator()
            break
        elif c==3:
            setting()
            break
        else:
            print("OPTION NOT AVAILABLE ")
else:
    while True:        
        c = int(input("\n(1) Item shop \n(2) Billing \n(3) Log Out \n"))
        if c==1:
            item_shop()
        elif c==2:
            billing()
            break
        elif c==3:
            break
        else:
            print("OPTION NOT AVAILABLE ")        
    

print("THANK YOU FOR USING OUR SOFTWARE \nHAVE A NICE DAY :) ")   
