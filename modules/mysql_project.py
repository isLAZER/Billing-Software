#Importing modules
from modules.mysql_init import *
from beautifultable import BeautifulTable


def displaySpecific(field,table,exp):
    tb=BeautifulTable()
    mysql_csr.execute(f"SELECT DISTINCT({field}) FROM {table} order by {field}")
    data = mysql_csr.fetchall()
    tb.columns.header = [exp+" List:-"]
    for i in data:
        tb.rows.append(i)
    print(tb)


def getall():
    mysql_csr.execute("select * from productInfo order by ITEM_CODE ")
    data = mysql_csr.fetchall()
    table=BeautifulTable()
    table.columns.header = ['CODE','NAME','CATEGORY','PRICE','DISCOUNT','BRAND']
    for i in data:
        table.rows.append(i)
    return table

#This function returns the list of the selected item                      
def getproduct(code,field):
    mysql_csr.execute(f'SELECT * from {field} ')
    data=mysql_csr.fetchall()
    for row in data:
        if code.upper()==row[0].upper():
            return list(row)

#This function displays the information of the selected item                      
def displayitem(code):
    mysql_csr.execute('SELECT * from productInfo;')
    data=mysql_csr.fetchall()
    for row in data:
        if code.upper()==row[0].upper():
            return 'Product code is: '+str(row[0])+'\nProduct name is: '+str(row[1])+'\nStock of that item: '+str(row[2])+'\nPrice of each item is: '+str(row[3])+'\nCategory of this item is: '+str(row[2])+'\n'
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
    while True:
        c=int(input("(1) Check current sales\n(2) Check Amount Paid to the suppliers\n(3) Check Profit on a Product\n(4) VIew profit chart \n..> "))
        if c==1:
            print("in work")
        
        elif c==4:
            print("Profit chart")
            mysql_csr.execute("SELECT ITEM_CODE,ITEM_NAME,BRAND,PRICE,POSBL_EARN,AMT_PAID,TOTAL_AMT_PAID,PROFITS FROM stocks ")
            data=mysql_csr.fetchall()
            table = BeautifulTable()
            table.columns.header=["ITEM_CODE",'NAME','BRAND','PRICE(per pc.)','TOTAL',"AMOUNT_PAID(per pc.)",'TOTAL_AMT_PAID',"PROFIT"]
            for row in data:
                table.rows.append(row)
            print(table)


def getstock(code):
    mysql_csr.execute(f"SELECT * from stocks where ITEM_CODE='{code}' ")
    data=mysql_csr.fetchall()
    table = BeautifulTable()
    table.columns.header = ["ITEM_CODE",'NAME','BRAND','PRICE(per pc.)','STOCK','STATUS','TOTAL',"AMOUNT_PAID(per pc.)",'TOTAL_AMT_PAID',"PROFIT","SUPPLIER_ID"]
    for row in data:
        table.rows.append(row)
    print(table)

def supplier_info(mode,code=None):
    query="SELECT ITEM_CODE,ITEM_NAME,BRAND,SUPPLIER_ID,SUPP_NAME FROM stocks,supplier WHERE stocks.SUPPLIER_ID=supplier.SUPP_ID "
    if mode==0:
        mysql_csr.execute("SELECT SUPP_ID,SUPP_NAME,CONTACT,LOCATION FROM supplier")
        data=mysql_csr.fetchall()
        table = BeautifulTable()
        table.columns.header = ['SUPPLIER_ID','SUPPLIER_NAME','CONTACT','LOACTION']
        for row in data:
            table.rows.append(row)
        print(table) 

    elif mode==1:
        mysql_csr.execute(query)
        data=mysql_csr.fetchall()
        table = BeautifulTable()
        table.columns.header = ['ITEM_CODE','NAME','BRAND','SUPPLIER_ID','SUPPLIER_NAME']
        for row in data:
            table.rows.append(row)
        print(table)

    elif mode==2:
        mysql_csr.execute(query+f"and ITEM_CODE='{code}'")
        data=mysql_csr.fetchall()
        table = BeautifulTable()
        table.columns.header = ['ITEM_CODE','NAME','BRAND','SUPPLIER_ID','SUPPLIER_NAME']
        for row in data:
            table.rows.append(row)
        return table  
    else:
        print("not a valid mode!")





