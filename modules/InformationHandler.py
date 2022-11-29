#Importing modules
import pickle
#Defininng the function
def Information():
    Info = open("Backend/information.dat","wb")
    Store_Name = str(input("Enter the store ID :"))
    Store_Mobile_No=str(input("Enter the Store Moblie number: "))
    Store_Address=input('Enter the Store Address: ')
    Store_GSTID=input('Enter GST invoice id: ')
    
    #Writing the information to the file
    pickle.dump([Store_Name,Store_Mobile_No,Store_Address,Store_GSTID],Info)
    Info.close()