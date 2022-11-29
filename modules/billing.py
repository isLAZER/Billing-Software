#Importing modules
from modules.mysql_init import *
from  modules.mysql_project import *
from beautifultable import BeautifulTable


def item_shop():
    while True:

        print("Search:-")    
        print()
        c = input("(1) Search Item name \n(2) Search Brand name\n(3) Search Category\n[Press X to exit search]\n>>>")
        print()
        if c == 1:
            itm = input("enter item name to be searched: ")
            try:
                mysql_csr.execute(f"SELECT * FROM productInfo where ITEM_NAME = {itm} ")
                data = mysql_csr.fetchall()
                table = BeautifulTable()
                table.columns.header = ['Search results']
                table.append(data)
                print(table)
            except:
                print("No item Found :(")
        elif c == 2:
            try:
                itm = input("enter brand name to be searched: ")
                mysql_csr.execute(f"SELECT * FROM productInfo where BRAND_NAME = {itm} ")
                data = mysql_csr.fetchall()
                table = BeautifulTable()
                table.columns.header = ['Search results']
                table.append(data)
                print(table)
            except:
                print("No item Found :(")
        elif c == 3:
            try:
                itm = input("enter brand name to be searched: ")
                mysql_csr.execute(f"SELECT * FROM productInfo where CATEGORY = {itm} ")
                data = mysql_csr.fetchall()
                table = BeautifulTable()
                table.columns.header = ['Search results']
                table.append(data)
                print(table)
            except:
                print("No item Found :(")

        else:
            break
        

    

#Defining the function 
def billing():    
    bill={}
    while True:
        print()
        x=input('(1) Add product to cart\n(2) Remove product from cart\n(3) Displaying information of a particular item\n(4) Displaying the items in cart\n(5) CHECKOUT\n>>> ')
        
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
    


            
        
