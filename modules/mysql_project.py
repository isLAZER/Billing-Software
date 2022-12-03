#Importing modules
from modules.mysql_init import *
from beautifultable import BeautifulTable


#stock queries
stockviewquery='SELECT productinfo.ITEM_CODE,ITEM_NAME,BRAND,STORED_ITEMS-STOCK AS SOLD,STOCK AS CURRENT_STOCK FROM stocks,productinfo,item_storage WHERE productinfo.ITEM_CODE=stocks.ITEM_CODE AND productinfo.ITEM_CODE=item_storage.ITEM_CODE'
categorystockquery="SELECT productinfo.ITEM_CODE,ITEM_NAME,BRAND,STOCK,CATEGORY FROM productinfo,stocks WHERE productinfo.ITEM_CODE=stocks.ITEM_CODE "

def stock_cat(code):
    mysql_csr.execute(categorystockquery+f"AND CATEGORY = {code}")
    data=mysql_csr.fetchall()
    table = BeautifulTable()
    table.columns.header=["CODE",'NAME','BRAND','STOCK','CATEGORY']
    for i in data:
        table.rows.append(i)
    return table

def status_list(data):
    lst=stock_status()
    for i in lst:
        a=list(data)
        a.append(i)
    return a


#check stocks
def check_stock(code=None):
    query=('SELECT STOCK from stocks ')
    if code==None:
        mysql_csr.execute(query)
        data=mysql_csr.fetchall()
        for row in data:
            return int(row[0])
    else:
        mysql_csr.execute(query+f" where ITEM_CODE='{code}' ")
        data=mysql_csr.fetchall()
        for row in data:
            return int(row[0])


#display specific stock
def getstockinfo(code):
    stockviewquery='SELECT productinfo.ITEM_CODE,ITEM_NAME,BRAND,STORED_ITEMS-STOCK AS SOLD,STOCK AS CURRENT_STOCK FROM stocks,productinfo,item_storage WHERE productinfo.ITEM_CODE=stocks.ITEM_CODE AND productinfo.ITEM_CODE=item_storage.ITEM_CODE'
    mysql_csr.execute(stockviewquery+f"AND productinfo.ITEM_CODE ='{code}' ")
    data=mysql_csr.fetchall()
    table = BeautifulTable()
    table.columns.header = ["CODE",'NAME','BRAND','ITEMS SOLD','STOCK']
    for row in data:
        table.rows.append(row)
    print(table)


#display perticular rec
def displaySpecific(field,table,exp):
    tb=BeautifulTable()
    mysql_csr.execute(f"SELECT DISTINCT({field}) FROM {table} order by {field}")
    data = mysql_csr.fetchall()
    tb.columns.header = [exp+" List:-"]
    for i in data:
        tb.rows.append(i)
    print(tb)

#returns a specific rec
def getproductinfo(code):
    mysql_csr.execute(f"select * from productinfo where ITEM_CODE ='{code}'")
    data = mysql_csr.fetchall()
    table=BeautifulTable()
    table.columns.header = ['CODE','NAME','PRICE','DISCOUNT','BRAND','CATEGORY']
    for i in data:
        table.rows.append(i)
    return table

#gets all the rec
def getall():
    mysql_csr.execute("select * from productInfo order by ITEM_NAME ")
    data = mysql_csr.fetchall()
    table=BeautifulTable()
    table.columns.header = ['CODE','NAME','PRICE','DISCOUNT','BRAND','CATEGORY']
    for i in data:
        table.rows.append(i)
    return table

#returns the list of the selected item                      
def getproduct(code,field):
    mysql_csr.execute(f'SELECT * from {field} ')
    data=mysql_csr.fetchall()
    for row in data:
        if code.upper()==row[0].upper():
            return list(row)

#displays the information of the selected item                      
def displayitem(code,field):
    mysql_csr.execute(f'SELECT * from {field}')
    data=mysql_csr.fetchall()
    for row in data:
        if code.upper()==row[0].upper():
            return 'Product code: '+str(row[0])+'\nProduct name: '+str(row[1])+'\nCategory: '+str(row[2])+'\nPrice: '+str(row[3])+'\nDiscount: '+str(row[4])+'\nBrand: '+str(row[5])+'\n'
    else:
        return 1

#update a sepcific field 
def update(code,field,exp):
    print("Selected Record:-")
    print(getproductinfo(code,'productInfo'))
    try:
        new=input("Enter New "+exp+": ")
        mysql_csr.execute(f"UPDATE productinfo SET {field} = '{new}' WHERE ITEM_CODE = '{code}' ")
        ms.commit()
        print("Entry updated!")
        print()
    except:
        print("Some error occured!\nTry again later...")

#add the items in a bill 
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
            total=z*n[2]
            bill.append([n[0],n[1],n[4],n[5],z,total,n[2]])
            print("ITEM ADDED TO THE BILL\n")
            return bill
        else:
            print("Entered quantity is more than that in stock\n")      
    else:
        print("Item code not found!")

#removes an item or a specific quantity 
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


#gets supplier info
def supplier_info(mode,code=None):
    query="SELECT productinfo.ITEM_CODE,ITEM_NAME,BRAND,SUPP_NAME,CONTACT FROM supplier,productinfo,stocks WHERE productinfo.ITEM_CODE=stocks.ITEM_CODE AND stocks.SUPPLIER_ID=supplier.SUPP_ID"
    #supplier basic
    if mode==0:
        mysql_csr.execute("SELECT * FROM supplier")
        data=mysql_csr.fetchall()
        table = BeautifulTable()
        table.columns.header = ['SUPPLIER_ID','SUPPLIER_NAME','CONTACT','LOACTION']
        for row in data:
            newlist=row[1:]
            table.rows.append(newlist)
        print(table) 
    #all supplier info 
    elif mode==1:
        mysql_csr.execute(query)
        data=mysql_csr.fetchall()
        table = BeautifulTable()
        table.columns.header = ['CODE','NAME','BRAND','SUPPLIER_NAME','CONTACT']
        for row in data:
            table.rows.append(row)
        print(table)
    #specific supplier info
    elif mode==2:
        mysql_csr.execute(query+f"and productinfo.ITEM_CODE='{code}'")
        data=mysql_csr.fetchall()
        table = BeautifulTable()
        table.columns.header = ['CODE','NAME','BRAND','SUPPLIER_NAME','CONTACT']
        for row in data:
            table.rows.append(row)
        return table  
    else:
        print("not a valid mode!")

#get a list of stock status
def stock_status():
    lst=check_stock()
    flag=[]
    for i in lst:
        if i<=10:
            flag.append('Low on stock')
        elif i==0:
            flag.append('Out of stock')
        else:
            flag.append('instock')
    return flag






