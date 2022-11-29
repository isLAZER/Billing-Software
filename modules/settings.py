#Importing modules
import pickle 
from modules.InformationHandler import *
def setting():
    c=int(input('1) Change the username and password\n2) Change the store information\n>'))
    if c==1:
        credintials_file = open("Backend/.admin.dat","wb")
        username =input("Enter the username you want : ")
        password = input("Enter the password you want : ")
        pickle.dump([username,password], credintials_file)
        credintials_file.close()
    if c==2:
        Information()