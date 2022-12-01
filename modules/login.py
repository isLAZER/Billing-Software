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
        cred = open("Backend/user_cred.dat","rb")
        data = pickle.load(cred)
        for i in data:
            if i[0] == user and i[1] == passwd:
                print(f"Welcome {user}!!!")
            else:
                cred.close()
                cred = open("Backend/user_cred.dat","wb")
                pickle.dump(data+[[user,passwd]],cred)
                print(f"New User Detected. Signup completed as {user}!!!")
        return str(user)

credentials.close()