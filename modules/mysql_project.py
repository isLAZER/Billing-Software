#Importing modules
from modules.mysql_init import *
from beautifultable import BeautifulTable

def check_stock(code):
    mysql_csr.execute(f"SELECT STOCK from stocks where ITEM_CODE='{code}' ")
    data=mysql_csr.fetchall()
    for row in data:
        return int(row[0])


def displaySpecific(field,table,exp):
    tb=BeautifulTable()
    mysql_csr.execute(f"SELECT DISTINCT({field}) FROM {table} order by {field}")
    data = mysql_csr.fetchall()
    tb.columns.header = [exp+" List:-"]
    for i in data:
        tb.rows.append(i)
    print(tb)

def getrec(code,field):
    mysql_csr.execute(f"select * from {field} where ITEM_CODE ='{code}'")
    data = mysql_csr.fetchall()
    table=BeautifulTable()
    table.columns.header = ['CODE','NAME','CATEGORY','PRICE','DISCOUNT','BRAND']
    for i in data:
        table.rows.append(i)
    return table


def getall():
    mysql_csr.execute("select * from productInfo order by ITEM_NAME ")
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
def displayitem(code,field):
    mysql_csr.execute(f'SELECT * from {field}')
    data=mysql_csr.fetchall()
    for row in data:
        if code.upper()==row[0].upper():
            return 'Product code: '+str(row[0])+'\nProduct name: '+str(row[1])+'\nCategory: '+str(row[2])+'\nPrice: '+str(row[3])+'\nDiscount: '+str(row[4])+'\nBrand: '+str(row[5])+'\n'
    else:
        return 1

#This function will add the items in a bill 
def append(code,bill):
    a=displayitem(code,'productInfo')
    print("\nItem description :>\n")
    n=getproduct(code,'productInfo')
    z=check_stock(code)
    if a!=1:
        print(str(a))
        quantity_utilised = int(input("Enter quantity: "))
        if z>=quantity_utilised:
            mysql_csr.execute(f'update stocks set stock =stock-{quantity_utilised} where Item_code = "{code}";')
            ms.commit()
            z=quantity_utilised
            total=z*n[3]
            bill.append([n[0],n[1],n[3],n[2],n[5],z,total])
            print("ITEM ADDED TO THE BILL\n")
            return bill
        else:
            print("Entered quantity is more than that in stock\n")      
    else:
        print("Item code not found!")

#This function removes a particular item or a specific quantity you want
def remove(code,bill):
    for i in bill:
        if i[0] == str(code.upper()):
            ch=int(input("(1)Remove all \n(2)Remove selected quantity\n..> "))
            if ch==1:
                bill.remove(i)
                print("ITEMS REMOVED")
            elif ch==2:
                print("Current quantity: ",str(i[5]))
                n = int(input("Enter quantity to remove: "))
                if n < i[5]:
                    i[5] -= n
                    mysql_csr.execute(f'update stocks set stock = stock+{n} where Item_code = "{code}" ')
                    ms.commit()
                    print(f'{n} items removed')
                elif n == bill[5]:
                    bill.pop(i)
                    mysql_csr.execute(f'update stocks set stock = stock+{n} where Item_code = "{code}" ')
                    ms.commit()
                    print("ITEM REMOVED")
                else:
                    print("ENTERED QUANTITY IS MORE THAN THAT WHAT YOU HAVE IN YOUR CART!!!\n")
        else:
            print("Wrong input")

def getstock(code):
    mysql_csr.execute(f"SELECT * from stocks where ITEM_CODE='{code}' ")
    data=mysql_csr.fetchall()
    table = BeautifulTable()
    table.columns.header = ["ITEM_CODE",'NAME','BRAND','PRICE','STOCK','STATUS',"SUPPLIER_ID"]
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


def update(code,field,exp):
    print("Selected Record:-")
    print(getrec(code,'productInfo'))
    try:
        new=input("Enter New "+exp+": ")
        mysql_csr.execute(f"UPDATE productinfo SET {field} = '{new}' WHERE ITEM_CODE = '{code}' ")
        ms.commit()
        print("Entry updated!")
        print()
    except:
        print("Some error occured!\nTry again later...")


