#Importing modules
from modules.mysql_init import *
from modules.mysql_project import *
from beautifultable import BeautifulTable


def register():
    while True:
        c=int(input("\n(1) Check Profit on a Product\n(2) Calculate Target amount to earn\n(2) Check Amount Paid to the suppliers\n(4) VIew profit chart \n(5) Exit\n..> "))
        if c==1:
            code=input("Enter the product code to be checked: ")
            print("Product status:-")
            mysql_csr.execute(f"SELECT ITEM_CODE,ITEM_NAME,BRAND,PROFITS FROM register where ITEM_CODE ='{code}'")
            data=mysql_csr.fetchall()
            table = BeautifulTable()
            table.columns.header=["ITEM_CODE",'NAME','BRAND','PROFIT']
            for row in data:
                table.rows.append(row)
            print(table)
            
        elif c==2:
            print()
            mysql_csr.execute("SELECT ITEM_CODE,ITEM_NAME,PRICE,STOCK,PRICE*STOCK as TARGET_AMT FROM register ")
            data=mysql_csr.fetchall()
            table = BeautifulTable()
            table.columns.header=["ITEM_CODE",'NAME','PRICE','STOCK','TARGET']
            for row in data:
                table.rows.append(row)
            print(table)

        elif c==3:
            print("Supplier logs:-")
            mysql_csr.execute("ITEM_CODE,ITEM_NAME,BRAND,AMT_PAID,SUPP_NAME,AMT_PAID*STOCK as TOTAL_PAID FROM register,supplier where SUPP_ID=SUPPLIER_ID")
            data=mysql_csr.fetchall()
            table = BeautifulTable()
            table.columns.header=["ITEM_CODE",'NAME','BRAND','STOCK',"AMOUNT_PAID(per pc.)",'TOTAL_PAID']
            for row in data:
                table.rows.append(row)
            print(table)

        
        elif c==4:
            print("Profit chart:-")
            mysql_csr.execute("SELECT ITEM_CODE,ITEM_NAME,BRAND,PRICE,AMT_PAID*STOCK,PRICE*STOCK - AMT_PAID*STOCK AS PROFITS FROM register ")
            data=mysql_csr.fetchall()
            table = BeautifulTable()
            table.columns.header=["ITEM_CODE",'NAME','BRAND','PRICE','TOTAL_AMT_PAID',"PROFIT"]
            for row in data:
                table.rows.append(row)
            print(table)

        elif c==5:
            break
        else:
            print("\nWrong input!")
            continue



