#Importing modules
from modules.mysql_init import *


#This function returns the list of the selected item                      
def getproduct(code):
    mysql_csr.execute('SELECT * from productInfo;')
    data=mysql_csr.fetchall()
    for row in data:
        if code.lower()==row[0].lower():
            return list(row)

#This function displays the information of the selected item                      
def displayitem(code):
    mysql_csr.execute('SELECT * from productInfo;')
    data=mysql_csr.fetchall()
    for row in data:
        if code.lower()==row[0].lower():
            return 'Product code is: '+str(row[0])+'\nProduct name is: '+str(row[1])+'\nStock of that item: '+str(row[2])+'\nPrice of each item is: '+str(row[3])+'\nCategory of this item is: '+str(row[4])+'\n'
    else:
        return 1              
#This function will add the items in a bill 
def append(code,bill):
    a=displayitem(code)
    print("Item description :>\n")
    n=getproduct(code)
    if a!=1:
        print(str(a))
        quantity_utilised = int(input("Enter the number of items you want: "))
        if n[2]>=quantity_utilised:
            mysql_csr.execute(f'update productInfo set stocks =stocks-{quantity_utilised} where Item_code = "{code.upper()}";')
            ms.commit()
            n[2]=quantity_utilised
            bill[code]=n
            print("ITEM ADDED TO THE BILL\n")
        else:
            print("Entered quantity is more than that in stock\n")
    else:
        print("code not found")
#This function removes a particular item or a specific quantity you want
def remove(code,bill):
    print("(1)Reomove all \n(2)Remove selected quantity\n")
    ch=input("Choose from above:")
    if ch=='1':
        bill.pop(code)
        print("ITEM REMOVED")
    elif ch =='2':
        n= int(input("how many products you want to remove:"))
        if n <bill[code][2]:
            bill[code][2]-=n
            mysql_csr.execute(f'update productInfo set stocks =stocks+{n} where Item_code = "{code.upper()}";')
            ms.commit()
            print(f'{n} number of items removed')
        elif n ==bill[code][2]:
            bill.pop(code)
            mysql_csr.execute(f'update productInfo set stocks =stocks+{n} where Item_code = "{code.upper()}";')
            ms.commit()
            print("ITEM REMOVED")
        else:
            print("ENTERED QUANTITY IS MORE THAN THAT WHAT YOU HAVE IN YOUR CART!!!\n")

def register():
    c=int(input("(1) Check current sales\n(2) "))