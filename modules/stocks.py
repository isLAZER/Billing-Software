#Importing modules
from  modules.mysql_project import *
from modules.mysql_init import *
from beautifultable import *


#Defing the function 
def shop():
    while True:
        print()
        x=int(input('(1) VIEW THE ITEM SHOP\n(2) ADD NEW ITEM ENTRY\n(3) REMOVE ITEM ENTRY\n(4) UPDATE AN ENTRY\n(5) Exit\n..> '))
        #display item shop
        if x==1:
            mysql_csr.execute('SELECT * from itemshop')
            data=mysql_csr.fetchall()
            count=mysql_csr.rowcount
            table = BeautifulTable()
            table.columns.header=["ITEM_CODE",'ITEM_NAME','BRAND','CATEGORY','PRICE','DISCOUNT']
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
            mysql_csr.execute(f"insert into productInfo values('{i_code}','{i_name}',{i_catg},'{i_price}','{i_dis}%','{i_brand}')")
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
        
        #complex updating part 


def stocks():
    while True:
        print()
        x=int(input('(1) VIEW STOCKS\n(2) UPDATE STOCKS \n(3) Exit\n..> '))
        #display stock details
        if x==1:
            mysql_csr.execute('SELECT * from stocks')
            data=mysql_csr.fetchall()
            count=mysql_csr.rowcount
            table = BeautifulTable()
            table.columns.header=["ITEM_CODE",'NAME','BRAND','PRICE(per pc.)','STOCK','STATUS','TOTAL',"AMOUNT_PAID(per pc.)",'TOTAL_AMT_PAID',"PROFIT","SUPPLIER_ID"]
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
                c=int(input("(1) Update the amount of stock for an item\n(2) Update status of a stock\n(3) Change supplier info \n..>"))
                if c==1:
                    code=input('Enter the Code of the Item to update stocks of: ')
                    getstock(code)
                    print()
                    new_val=int(input("Enter the stock value to be added: "))
                    try:
                        mysql_csr.execute(f"UPDATE stocks SET STOCKS = stocks+{new_val} where ITEM_CODE='{code}'")
                        ms.commit()
                    except :
                        print(f"SOME ERROR HAPPENED AT OUR END!\nPLEASE RETRY ")
                        continue

                elif c==2:
                    code=input('Enter the Code of the Item to update stocks of: ')
                    getstock(code)
                    print()
                    while True:
                        print("[\t out of stock -0\n instock - 1\n low on stock -2\t]")
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
                            break
                        print("Update completed!")
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
                    except:
                        print(f"SOME ERROR HAPPENED AT OUR END!\nPLEASE RETRY ")
                        continue

        if x==3:
            break
