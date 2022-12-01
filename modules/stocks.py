#Importing modules

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
            mysql_csr.execute(f"insert into itemshop values('{i_code}','{i_name}','{i_brand}','{i_catg}','{i_price}/-','{i_dis} %')")
            ms.commit()
            print("ITEM ADDED TO DATABASE!")
        
        #deleting an entry
        elif x==3:
            code=input("Enter the code of the item you want to remove from database: ")
            try:
                mysql_csr.execute(f"DELETE FROM productInfo WHERE Item_code='{code}';  ")
                print("Item removed from datbase ")
                ms.commit()
            except:
                print("AN ERROR OCCURRED\nFAILED TO DELETE ENTRY!")
        
        #complex updating part 


def stocks():
    while True:
        print()
        x=int(input('(1) VIEW STOCKS\n(2) UPDATE STOCKS \n(5) Exit\n..> '))
        #display stock details
        if x==1:
            mysql_csr.execute('SELECT * from stocks')
            data=mysql_csr.fetchall()
            count=mysql_csr.rowcount
            table = BeautifulTable()
            table.columns.header=["ITEM_CODE",'ITEM_NAME','BRAND','PRICE','STOCK','STATUS']
            if count == 0:
                print("No Item in stock!")
            else:
                for row in data:
                    table.rows.append(row)    
            print()
            print(table)
        #updating stocks
        elif x==2:
            cod=input('Enter the Code of the Item to update stocks of: ')
            #work in progress 
            # features
            # 1. update the amt in stock
            # 2. update status of stock
            # 3. profit count
            
        '''
        
        #Below code will REMOVE an item from stock
        if x==3:
            
        #Below code will increase the number of items in stock
        if x==4:
            code = input("Enter the code of the item of which you want to increase: ")
            new_quantity = int(input("Enter the number of new item : "))
            try:
                mysql_csr.execute(f"UPDATE productInfo set stocks =stocks+{new_quantity} where Item_code='{code.strip()}'")
                ms.commit()
            except :
                print(f"SOME ERROR HAPPENED AT OUR END!\n PLEASE RETRY ")
        '''                    
        #EXIT
        if x==5:
            break
