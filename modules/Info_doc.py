#Importing modules
import pickle

#Defininng the functions
#function 1
def Info_display():
    print('\nShop Info:')
    info= open("Backend/shop_information.dat","rb")
    data=pickle.load(info)
    print('Store Id: ',data[0])
    print('Store Name: ',data[1])
    print('Contact: ',data[2])
    print('Address: ',data[3])
    print('GST invoice: ',data[4])
    print('Description: ',data[5])
    
    info.close()

#function 2
def Info_input():
    print('Info:')
    Store_id = input("Enter store id :")
    Store_Name = str(input("Enter the store name :"))
    Store_Contact = str(input("Enter the store contact number: "))
    Store_Address=input('Enter the Store Address: ')
    Store_GSTID=input('Enter GST invoice id: ')
    Store_Discription=input('Enter Store description: ')
    
    #Writing the information to the file
    Info = open("Backend/shop_information.dat","wb")
    pickle.dump([Store_id,Store_Name,Store_Contact,Store_Address,Store_GSTID,Store_Discription] , Info)
    print("Information updated!")
    Info.close()


#gets customer info to make bill        
def customer_info():
    print("\nBilling details:-")
    name=input("Enter your name: ")
    contact=int(input("Enter youe phone number: "))
    pay=int(input("Enter payment method\n[> (0) - Cash\n > (1) - Online\n > (2) - Debit/Credit ]\n..> "))
    if pay==0:
        mode='Cash'
    if pay==1:
        mode='Online'
    elif pay==2:
        mode='Debit/Credit'

    data=[name,contact,mode]
    return data  

