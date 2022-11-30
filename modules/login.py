#Importing modules
import pickle
credentials = open("Backend/login_info.dat","rb")
info=pickle.load(credentials)
username=info['user']
password=info['pass']
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


