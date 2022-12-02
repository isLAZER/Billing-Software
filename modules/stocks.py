#Importing modules
from  modules.mysql_project import *
from modules.mysql_init import *
from beautifultable import *


#Defing the function 
#display shop
def shop():
    while True:
        x=int(input('\nMenu:-\n(1) VIEW THE ITEM SHOP\n(2) ADD NEW ITEM ENTRY\n(3) REMOVE ITEM ENTRY\n(4) CHANGE AN ENTRY\n(5) Exit\n..> '))
        #display item shop
        if x==1:
            mysql_csr.execute('SELECT * from productinfo')
            data=mysql_csr.fetchall()
            count=mysql_csr.rowcount
            table = BeautifulTable()
            table.columns.header=["ITEM_CODE",'ITEM_NAME','BRAND','PRICE','DISCOUNT','CATEGORY']
            
            if count == 0:
                print("No Items in shop currently!")
            else:
                for row in data:
                    table.rows.append(row)        
            print(table)
        
        #Adding new entry 
        elif x==2:
            i_code=input("Enter the Item code : ")
            i_name=input("Enter the Item name : ")
            i_brand=input('Enter the Brand name : ')
            i_price =input("Enter the rate per item: ")
            i_catg=input('Enter the category of that item: ')
            i_dis=input("Enter the discount percentage : ")
            mysql_csr.execute(f"insert into productInfo values('{i_code}','{i_name}','{i_catg}','{i_price}','{i_dis}','{i_brand}')")
            ms.commit()
            print("ITEM ADDED TO DATABASE!")
        
        #deleting an entry
        elif x==3:
            code=input("Enter the code of the item you want to remove from database: ")
            try:
                mysql_csr.execute(f"DELETE FROM itemshop WHERE Item_code='{code}';  ")
                print("Item removed from datbase ")
                ms.commit()
            except:
                print("AN ERROR OCCURRED\nFAILED TO DELETE ENTRY!")
        
        #updating an entry 
        elif x==4:
            while True:
                a = int(input("What do you want to Update\n(1) Change Name\n(2) Change Brand name\n(3) Change category\n(4) Change Price\n(5) Change Discount\n..> "))
                code=input("Enter the item code to update data: ")
                if a==1:
                    update(code,'ITEM_NAME','Name')
                elif a==2:
                    update(code,'BRAND','Brand Name')
                elif a==3:
                    update(code,'CATEGORY','Category')
                elif a==4:
                    update(code,'PRICE','Rate per item')
                elif a==5:
                    update(code,'DISCOUNT','Discount %')
                else:
                    print('Wrong input!')
                    continue
                print("Updated Record:-\n",getrec(code,'productInfo'))
                print()
                ch=input("Want to continue updating?(Y/N): ")
                if ch=='y' or ch=='Y':
                    print()
                    continue  
                else:
                    break
        #exit
        elif x==5:
            break
        else:
            print('Wrong input!')
            continue

#manage stocks
def stocks():
    while True:
        x=int(input('\nMenu:-\n(1) VIEW STOCKS\n(2) UPDATE STOCKS \n(3) Exit\n..> '))
        #display stock details
        if x==1:
            mysql_csr.execute('SELECT * from stocks')
            data=mysql_csr.fetchall()
            count=mysql_csr.rowcount
            table = BeautifulTable()
            table.columns.header=["ITEM_CODE",'NAME','BRAND','PRICE(per pc.)','STOCK','STATUS',"SUPPLIER_ID"]
            if count == 0:
                print("No Item in stock!")
            else:
                for row in data:
                    table.rows.append(row)    
            print()
            print(table)
        
        #updating stocks
        elif x==2:
            while True:
                c=int(input("(1) Update stock amount for an item\n(2) Update status of a stock\n(3) Change supplier info \n..> "))
                if c==1:
                    code=input('Enter the Code of the Item to update stocks of: ')
                    getstock(code)
                    print()
                    new_val=int(input("Enter the stock value to be added: "))
                    try:
                        mysql_csr.execute(f"UPDATE stocks SET STOCK = stock+{new_val} where ITEM_CODE='{code}'")
                        ms.commit()
                        print("Amount updated!")
                        print()
                        print("Updated Record:-")
                        getstock(code)
                    except :
                        print(f"SOME ERROR HAPPENED AT OUR END!\nPLEASE RETRY ")
                        continue

                elif c==2:
                    code=input('Enter the Code of the Item to update stocks of: ')
                    getstock(code)
                    print()
                    while True:
                        print("[ > 0- out of stock \n  > 1- instock \n  > 2- low on stock  ]")
                        z=int(input("Enter the status from above menu: "))

                        if z==0:
                            mysql_csr.execute(f"UPDATE stocks SET STATUS = 'out of stock' where Item_code='{code}'")
                            ms.commit()
                        elif z==1:
                            mysql_csr.execute(f"UPDATE stocks SET STATUS = 'instock' where Item_code='{code}'")
                            ms.commit()
                        elif z==2:
                            mysql_csr.execute(f"UPDATE stocks SET STATUS = 'low on stock' where Item_code='{code}'")
                            ms.commit()
                        else:
                            print("Wrong input\nplease refer the status menu to put the correct number! ")
                            continue
                        print("Update completed!")
                        print()
                        print("Updated Record:-")
                        getstock(code)
                        
                        ch=input("\nWhat to continue updating?(Y/N): ")
                        if ch=='y' or ch=='Y':
                            print()
                            continue  
                        else:
                            break
                        
                elif c==3:
                    supplier_info(1)
                    code=input('Enter the Code of the Item to update supplier info of: ')
                    print()
                    
                    tb1=supplier_info(2,code)
                    print("Seleted field:-\n",tb1)
                    print()
                    print("Enter new Supplier id for table below:")
                    supplier_info(0)
                    new_code=input("Enter Code ..> ")
                    try:
                        mysql_csr.execute(f"UPDATE stocks SET SUPPLIER_ID = '{new_code}' WHERE ITEM_CODE = '{code}' ")
                        ms.commit()
                        print("Update Completed!")
                        print()
                        print("Updated Record:-\n")
                        getstock(code)
                    except:
                        print(f"SOME ERROR HAPPENED AT OUR END!\nPLEASE RETRY ")
                        continue

                ch=input("\nWhat to continue updating?(Y/N): ")
                if ch=='y' or ch=='Y':
                    print()
                    continue  
                else:
                    break

        #exit
        elif x==3:
            break
        else:
            print('Wrong input!')
            continue