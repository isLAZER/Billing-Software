#Importing modules
import pickle
#Defininng the function
def Information():
    
    Store_Name = str(input("Enter the store ID :"))
    Store_Contact = str(input("Enter the store contact number"))
    Mobile_No=str(input("Enter Owner's Moblie number: "))
    Store_Address=input('Enter the Store Address: ')
    Store_GSTID=input('Enter GST invoice id: ')
    Store_Discription=input('Enter Store description: ')
    
    #Writing the information to the file
    Info = open("Backend/information.dat","wb")
    pickle.dump([Store_Name,Store_Contact,Mobile_No,Store_Address,Store_GSTID,Store_Discription],Info)
    Info.close()