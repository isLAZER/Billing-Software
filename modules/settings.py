#Importing modules
import pickle 

#settings menu
def setting():
    while True:
        c=input('(1) Change admin username and password\n[Press X to exit]\n..> ')
        if c==1:
            file = open("Backend/admin.dat","wb")
            username = str(input("Enter the new username : "))
            while True:
                password = str(input("Enter a password : "))
                rec={'user':username,'pass':password}
                confirm_pass=str(input("Confirm password : "))
                if password==confirm_pass:
                    pickle.dump(rec,file)
                    print('Setup complete!\nUsername and Password changed...')
                    break
                else:
                    print("Error!\n---Please Retry!")
                    continue
            print()
            file.close()

        else:
            break