# Importing modules
import pickle
credentials = open("Backend/admin.dat", "rb")
info = pickle.load(credentials)
username = info['user']
password = info['pass']

# Login function


def login(user, passwd):
    # Checking for ADMIN access
    if user == username and passwd == password:
        print(f"Logged in as ADMIN ")
        return "ADMIN"
    else:
        cred = open("Backend/customer.dat", "rb")
        try:
            global data
            data = pickle.load(cred)
            for i in data:
                if i[0] == user and i[1] == passwd:
                    print(f'Logged in as "{user}"\nEnjoy the shopping :) ')
                    cred.close()
                    return str(user)
            cred.close()
            cred = open("Backend/customer.dat", "wb")
            pickle.dump(data+[[user, passwd]], cred)
            print(f"New User Detected. Signup completed!")
            print(f"Logged in as {user}")
            return str(user)
        except:
            cred.close()
            cred = open("Backend/customer.dat", "ab")
            pickle.dump([[user, passwd]], cred)
            print("New User Detected. Signup completed!")
            print(f"Logged in as {user}")
            return str(user)


credentials.close()
