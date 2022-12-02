#Importing modules
from modules.mysql_init import *
from  modules.mysql_project import *
from beautifultable import BeautifulTable


def item_shop():
    while True:
        print("Search:-")    
        print()
        c = eval(input("(1) Search Item name \n(2) Search Brand name\n(3) Search Category\n(4) View entire shop products\n[Press 0 to exit search]\n..> "))
        print()

        #item search
        if c==1:
            displaySpecific("ITEM_NAME","itemshop","item")
            try:
                itm = input("Enter item name to be searched: ")
                mysql_csr.execute(f"SELECT * from productInfo where ITEM_NAME='{itm}' order by ITEM_CODE ")
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
            displaySpecific("BRAND_NAME","BRAND","Brand")
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
            displaySpecific("CATEGORY_NAME","CATEGORY","Category")
            print(tb)
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
            tb=getall()
            print(tb)
            
        elif c==0:
            print("Search completed!")
            break
        else:
            print('Wrong input!')
            continue

        #continue option
        x=input("Continue search?(Y/N): ")
        if x=='y' or x=='Y':
            continue
        else:
            print("Search completed!")
            break
      

    

#Defining the function 
def billing():

    bill={}
    while True:
        print()
        print("{YOUR CART}")
        x=int(input('(1) Add product to cart\n(2) Remove product from cart\n(3) Displaying information of a particular item\n(4) Displaying the items in cart\n(5) CHECKOUT!\n..> '))
        
        #To append an item into the bill
        if x==1:
            code=input('Enter the code of the item you want to add to the bill: ')
            append(code,bill)
        #To remove an item from the bill
        elif x==2:
            code=input('Enter the code of the item you want to remove from the bill: ')   
            remove(code,bill)
        #To display information of an item    
        elif x==3:
            code=input('Enter the code of that item whose information is to be displayed: ')
            print(str(displayitem(code)))
        #Shows all items in your cart
        elif x==4:
            table = BeautifulTable()
            total=0
            table.columns.header = ["ITEM_CODE", "ITEM_NAME",'BRAND',"QUANTITY","RATE PER ITEM",'CATEGORY',"TOTAL COST/ITEM"]
            for key,value in bill.items():
                value.append(value[3]*value[4])
                table.rows.append(value)
                total +=value[6]
            table.rows.append([" "," "," "," "," ","TOTAL",total])
            print()
            print(table)
            
        #Below will checkout
        elif x==5:
            if bill!={}:
                import pickle
                infofile =open("Backend/information.dat","rb")
                try:
                    r=pickle.load(infofile)
                except:
                    pass
                infofile.close()
                
                print()
                print('STORE_ID: ',r[0])
                print()
                print(table)
                print('ADDRESS: ',r[2])
                print('MOBILE_NUMBER',r[1])
                print()
                print("THANK YOU FOR VISITING OUR STORE \nHAVE A NICE DAY!")
                print()
                break
            else:
                print("NO ITEM IN THE CART!")
        elif x=='X'or x=='x':
            exit()
        else:
            print("Entered option is not in menu")        
    


            
        
