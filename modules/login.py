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

'''
    if user==username and passwd==password:
        return "ADMIN"
    else:
        cred = open("Backend/customer.dat","rb")
        try:
            data = pickle.load(cred)
            for i in data:
                if i[0] == user and i[1] == passwd:
                    print(f"Welcome {user}!!!")
                    cred.close()
                return str(user)
        except:        
            cred.close()
            cred = open("Backend/customer.dat","wb")
            pickle.dump(data+[[user,passwd]],cred)
            print(f"New User Detected. Signup completed!")
            return str(user)
'''
credentials.close()