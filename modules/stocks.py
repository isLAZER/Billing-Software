#Importing modules

from modules.mysql_init import *
from beautifultable import *

#Defing the function 
def stocks():
    while True:
        x=int(input('(1) VIEW STOCKS\n(2) ADDING NEW ITEM IN  STOCKS\n(3) REMOVING STOCKS\n(4) UPDATE STOCKS \n(5) Exit\n> '))
        #Below code will show full stock
        if x==1:
            mysql_csr.execute('SELECT * from productInfo;')
            data=mysql_csr.fetchall()
            count=mysql_csr.rowcount
            table = BeautifulTable()
            table.columns.header=["ITEM_CODE",'ITEM_NAME','STOCK','PRICE','CATEGORY']
            if count == 0:
                print("No Items in stock currently!\nStock will be renewed soon :)")
            else:
                for row in data:
                    table.rows.append(row)
                
            print()
            print(table)
            
            
        #Below code will show ADD new item to stock
        if x==2:
            item_code=input("Enter the Item code : ")
            item_name=input("Enter the Item name : ")
            item_stocks=input('Enter the number of items: ')
            item_price =input("Enter the rate per item: ")
            category_item=input('Enter the category of that item: ')
            mysql_csr.execute(f"insert into productInfo values('{item_code}','{item_name}',{item_stocks},{item_price},'{category_item}');")
            ms.commit()
            print("ITEM ADDED TO DATABASE")
            
        #Below code will REMOVE an item from stock
        if x==3:
            code=input("Enter the code of the item you want to remove from database: ")
            try:
                mysql_csr.execute(f"DELETE FROM productInfo WHERE Item_code='{code}';  ")
                print("Item removed from datbase ")
                ms.commit()
            except:
                print("SOME ERROR HAPPENED AT OUR END :-(")
        #Below code will increase the number of items in stock
        if x==4:
            code = input("Enter the code of the item of which you want to increase: ")
            new_quantity = int(input("Enter the number of new item : "))
            try:
                mysql_csr.execute(f"UPDATE productInfo set stocks =stocks+{new_quantity} where Item_code='{code.strip()}'")
                ms.commit()
            except :
                print(f"SOME ERROR HAPPENED AT OUR END!\n PLEASE RETRY ")                    
        #EXIT
        if x==5:
            break
