#Importing modules
import pickle
#Defininng the function

def Info_display():
    info= open("Backend/shop_information.dat","rb")
    a=pickle.load(info)
    print()
    info.close()


def Info_input():
    Store_id = input("Enter store id :")
    Store_Name = str(input("Enter the store name :"))
    Store_Contact = str(input("Enter the store contact number"))
    Mobile_No=str(input("Enter Owner's Moblie number: "))
    Store_Address=input('Enter the Store Address: ')
    Store_GSTID=input('Enter GST invoice id: ')
    Store_Discription=input('Enter Store description: ')
    
    #Writing the information to the file
    Info = open("Backend/shop_information.dat","wb")
    pickle.dump([Store_id,Store_Name,Store_Contact,Mobile_No,Store_Address,Store_GSTID,Store_Discription],Info)
    Info.close()


def Information():
    while True:
        x=int(input("(1) Display info\n(2) Change info\n(3) Exit\n..> "))
        if x==1:
            Info_display()
        elif x==2:
            z=input("Press 'Y' to Confirm\n[the previous data will be lost forever]\n..> ")
            if z=='y' or z=='Y':
                Info_input()
            else:
                print("exit!")
                break
        elif x==3:
            break
        else:
            print("Wrong input!")
            break
