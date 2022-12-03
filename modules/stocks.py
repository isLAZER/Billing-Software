#Importing modules
from modules.mysql_project import *
from modules.mysql_init import *
from beautifultable import *


#Defing the function 
#display shop
def shop():
    while True:
        x=int(input('\nMenu:-\n(1) VIEW ITEM SHOP\n(2) ADD NEW ITEM ENTRY\n(3) REMOVE AN ITEM ENTRY\n(4) CHANGE EXISTING ENTRY\n(5) EXIT\n..> '))
        #display item shop
        if x==1:
            mysql_csr.execute('SELECT * from productinfo')
            data=mysql_csr.fetchall()
            count=mysql_csr.rowcount
            table = BeautifulTable()
            table.columns.header= ["CODE",'ITEM NAME','PRICE','DISCOUNT','BRAND','CATEGORY']
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
            mysql_csr.execute(f"insert into productInfo values('{i_code}','{i_name}','{i_price}','{i_dis}','{i_brand}','{i_catg}')")
            ms.commit()
            print("ITEM ADDED TO DATABASE!")
        
        #deleting an entry
        elif x==3:
            code=input("Enter the code of the item you want to remove from database: ")
            try:
                mysql_csr.execute(f"DELETE from productinfo WHERE Item_code='{code}';  ")
                print("Item removed from datbase ")
                ms.commit()
            except:
                print("Error!\nFAILED TO DELETE ENTRY!")
        
        #updating an entry 
        elif x==4:
            while True:
                a = int(input("What do you want to Change:\n(1) Change Name\n(2) Change Brand name\n(3) Change category\n(4) Change Price\n(5) Change Discount\n..> "))
                code=input("Enter item code to update data for: ")
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
                print("Updated Record:-\n",getproductinfo(code))
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


def status_list(data):
    new=[]
    l1=stock_status()
    for i in data:
        row=list(i)
        row.append(l1[0])
        l1.pop(0)
        new.append(row)
    return new


#manage stocks
def stocks():
    while True:
        x=int(input('\nMenu:-\n(1) VIEW STOCKS\n(2) UPDATE STOCKS \n(3) Exit\n..> '))
        #display stock details
        if x==1:
            mysql_csr.execute(stockviewquery)
            data=mysql_csr.fetchall()
            count=mysql_csr.rowcount
            table = BeautifulTable()
            table.columns.header=["CODE",'NAME','BRAND','ITEM SOLD','STOCK LEFT',' STATUS']
            if count == 0:
                print("No Item in stock!")
            else:
                newdata=status_list(data)
                for row in newdata:
                    table.rows.append(row)   
            print()
            print(table)
        
        #updating stocks
        elif x==2:
            while True:
                c=int(input('(1) Adding stock amount for an item\n(2) Adding stock based on category\n..> '))
                if c==1:
                    code=input('Enter the Code of the Item to update stocks of: ')
                    getstockinfo(code)
                    print()
                    quantity=int(input("Enter quantity to be added: "))
                    try:
                        mysql_csr.execute(f"UPDATE productinfo,stocks SET STOCK = STOCK+{quantity} where stocks.ITEM_CODE=productinfo.ITEM_CODE AND productinfo.ITEM_CODE='{code}' ")
                        ms.commit()
                        print("Amount updated!")
                        print()
                        print("Updated Record:-")
                        getstockinfo(code)
                    except :
                        print(f"SOME ERROR HAPPENED AT OUR END!\nPLEASE RETRY ")
                        continue
                elif c==2:
                    displaySpecific("CATEGORY","productinfo","Category")
                    code=input('Enter the Category of items to update stocks of: ')
                    table=stock_cat(code)
                    print("All products of selected category:-")
                    print(table)

                    #updating
                    print()
                    quantity=int(input("Enter quantity to be added to all items above: "))
                    try:
                        mysql_csr.execute(f"UPDATE productinfo,stocks SET STOCK = STOCK+{quantity} where stocks.ITEM_CODE=productinfo.ITEM_CODE AND productinfo.CATEGORY= '{code}' ")
                        ms.commit()
                        print("Amount updated!")
                        print()
                        print("Updated Record:-")
                        print(stock_cat(code))
                    except :
                        print(f"SOME ERROR HAPPENED AT OUR END!\nPLEASE RETRY ")
                        continue

                ch=input("\nWant to continue updating?(Y/N): ")
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


        