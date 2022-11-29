#Importing modules
import pickle
credentials = open("Backend/.admin.dat","rb")
information=pickle.load(credentials)
username=information[0]
password=information[1]
print("login :-")

#login function 
def login(user,passwd):
    #checking for ADMIN access
    if user==username and passwd==password:
        return "ADMIN"
    else:
        print(f"Logged in as {user}")
        return str(user)
    

credentials.close()


