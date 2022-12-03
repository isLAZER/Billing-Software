#Importing modules
from modules.mysql_init import *
from  modules.mysql_project import *
from beautifultable import BeautifulTable
from datetime import datetime
from modules.Info_doc import customer_info


#setting date and time
now = datetime.now()


def make_table(tb):
    table=BeautifulTable()
    total=0
    table.columns.header=["PRODUCT NAME","PRICE","CATEGORY","BRAND","QUANTITY","FINAL PRICE"]
    for i in tb:
        newlist=i[1:]
        table.rows.append(newlist)
        total+=i[5]
    table.rows.append([" "," "," "," ","TOTAL",total])
    return table


def item_shop():
    while True:
        print("Search:-")    
        print()
        c = eval(input("(1) Search Item name \n(2) Search Brand name\n(3) Search Category\n(4) Display details of a particular item\n(5) VIEW FULL ITEM SHOP\n(5) Exit\n..> "))
        print()

        #item search
        if c==1:
            displaySpecific("ITEM_NAME","productInfo","item")
            try:
                itm = input("Enter item name to be searched: ")
                mysql_csr.execute(f"SELECT * from productInfo where ITEM_NAME='{itm}' order by ITEM_NAME ")
                data = mysql_csr.fetchall()
                count=mysql_csr.rowcount
                table = BeautifulTable()
                table.columns.header = ['CODE','NAME','CATEGORY','PRICE', 'DISCOUNT','BRAND']
                for i in data:
                    table.rows.append(i)
                if count==0:
                    print("No item Found :(")
                else:
                    print('Search results -')
                    print(table)    
            except:
                print("No item Found :(")

            #continue option
            x=input("Continue search?(Y/N): ")
            if x=='y' or x=='Y':
                continue
            else:
                print("Search completed!")
                break 

        
        #brand search
        elif c==2:
            displaySpecific("BRAND","productInfo","Brand")
            try:
                itm = input("Enter Brand name to be searched: ")
                mysql_csr.execute(f"SELECT * from productInfo where BRAND ='{itm}' order by ITEM_NAME ")
                data = mysql_csr.fetchall()
                count=mysql_csr.rowcount
                table = BeautifulTable()
                table.columns.header = ['CODE','NAME','CATEGORY','PRICE', 'DISCOUNT','BRAND']
                for i in data:
                    table.rows.append(i)
                if count==0:
                    print("No item Found :(")
                else:
                    print('Search results -')
                    print(table)    
            except:
                print("No item Found :(")
 
        #category search
        elif c==3:
            displaySpecific("CATEGORY","productinfo","Category")
            try:
                itm = input("Enter Category to be searched: ")
                mysql_csr.execute(f"SELECT * from productInfo where CATEGORY ='{itm}' order by ITEM_NAME ")
                data = mysql_csr.fetchall()
                count=mysql_csr.rowcount
                table = BeautifulTable()
                table.columns.header = ['CODE','NAME','CATEGORY','PRICE', 'DISCOUNT','BRAND']
                for i in data:
                    table.rows.append(i)
                if count==0:
                    print("No item Found :(")
                else:
                    print('Search results -')
                    print(table) 
            except:
                print("No item Found :(")
        elif c==4:
            code=input('Enter the code of that item whose information is to be displayed: ')
            print(str(displayitem(code,'productInfo')))

        elif c==5:
            tb=getall()
            print(tb)
            x=input("Proceed to billing?(Y/N): ")
            if x=='y' or x=='Y':
                print("Search completed!")
                break  
            else:
                continue
            
        elif c==5:
            print("Search completed!")
            break
        else:
            print('Wrong input!')
            continue

        #continue option
        x=input("Continue Search?(Y/N): ")
        if x=='y' or x=='Y':
            continue
        else:
            print("Search completed!")
            break
        
      
#Defining the function 
def billing():
    bill=[]
    while True:
        print()
        x=int(input('[ YOUR CART ]\n(1) Add product to cart\n(2) Remove product from cart\n(3) Display all items in the cart\n(4) Proceed to checkout\n..> '))
        
        #To append an item into the bill
        if x==1:
            code=input('Enter the code of the item you want to add to the bill: ')
            append(code,bill)
        #To remove an item from the bill
        elif x==2:
            code=input('Enter the code of the item you want to remove from the bill: ')   
            remove(code,bill)   
    
        #Shows all items in your cart
        elif x==3:
            if bill!=[]:
                print("\nCART:-")
                print(make_table(bill))
            else:
                print("NO ITEM IN THE CART!")
                continue

        elif x==4:
            if bill!=[]:
                c=input("\n> Are you satisfied with your cart?(Y/N) ")
                if c=='y' or c=='Y':
                    return make_table(bill)
                else:
                    continue
            else:
                print("NO ITEM IN THE CART!")
                continue
        else:
            print("Entered option is not in menu")
            continue

def checkout(table):
    print()
    details=customer_info()
    import pickle
    infofile =open("Backend/shop_information.dat","rb")
    try:
        info=pickle.load(infofile)
    except:
        pass
    infofile.close()
    
    date_time = now.strftime("date:%d/%m/%Y\ntime:%H:%M:%S")
    print()
    print('--------------------------------------------------------------------------------')
    print()
    print('Customer Name: ',details[0])
    print('Customer Phone no.: ',details[1])
    print('Payment method: ',details[2])
    print()
    print('--------------------------------------------------------------------------------')
    print("                              ",info[1])
    print()
    print()
    print(date_time)
    print(table)
    print()
    print('STORE_ID: ',info[0])
    print('ADDRESS: ',info[3])
    print('CONTACT: ',info[2])
    print()
    print("THANK YOU FOR VISITING OUR STORE \nHAVE A NICE DAY!")
    print()
    print('--------------------------------------------------------------------------------')
    print()