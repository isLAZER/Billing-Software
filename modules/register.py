# Importing modules
from modules.mysql_init import *
from modules.mysql_project import *
from beautifultable import BeautifulTable


# register queries
profitquery = ("SELECT productinfo.ITEM_CODE,ITEM_NAME,BRAND,SELLING_PRICE-COST_PRICE AS EARNINGS,(SELLING_PRICE-COST_PRICE)*STOCK AS PROFIT FROM productinfo,stocks,register WHERE productinfo.ITEM_CODE=stocks.ITEM_CODE AND productinfo.ITEM_CODE=register.ITEM_CODE ")
supplierquery = ('SELECT productinfo.ITEM_CODE,ITEM_NAME,BRAND,SUPP_NAME,COST_PRICE*STOCK as INVESTMENT FROM register,supplier,stocks,productinfo WHERE SUPP_ID=SUPPLIER_ID AND productinfo.ITEM_CODE = stocks.ITEM_CODE AND productinfo.ITEM_CODE = register.ITEM_CODE ')
salesquery = ('SELECT productinfo.ITEM_CODE,ITEM_NAME,BRAND,SELLING_PRICE-COST_PRICE AS EARNINGS,STORED_ITEMS-STOCK AS NUM_SOLD,(SELLING_PRICE-COST_PRICE)*(STORED_ITEMS-STOCK) AS PROFIT FROM productinfo,stocks,register,item_storage WHERE productinfo.ITEM_CODE=stocks.ITEM_CODE AND productinfo.ITEM_CODE=register.ITEM_CODE AND productinfo.ITEM_CODE=item_storage.ITEM_CODE ')
max_salesquery = ('SELECT productinfo.ITEM_CODE,ITEM_NAME,BRAND,SELLING_PRICE-COST_PRICE AS EARNINGS,STORED_ITEMS-STOCK AS NUM_SOLD,MAX((SELLING_PRICE-COST_PRICE)*(STORED_ITEMS-STOCK)) AS PROFIT FROM productinfo,stocks,register,item_storage WHERE productinfo.ITEM_CODE=stocks.ITEM_CODE AND productinfo.ITEM_CODE=register.ITEM_CODE AND productinfo.ITEM_CODE=item_storage.ITEM_CODE')

# register menu


def register():
    while True:
        c = int(input("\n(1) Check Earnings as of today\n(2) Check Top seller as of today \n(3) Check Profit on a Product\n(4) View profit chart\n(5) VIew Supplier logs \n(6) Exit\n..> "))

        if c == 1:
            print()
            mysql_csr.execute(salesquery)
            data = mysql_csr.fetchall()
            table = BeautifulTable()
            table.columns.header = ["ITEM_CODE", '   NAME        ',
                                    'BRAND', 'EARNING PER ITEM', 'ITEMS SOLD', 'TOTAL PROFIT']
            for row in data:
                table.rows.append(row)
            print(table)

        elif c == 2:
            print()
            mysql_csr.execute(max_salesquery)
            data = mysql_csr.fetchall()
            table = BeautifulTable()
            table.columns.header = [
                "ITEM_CODE", 'BEST SELLER', 'BRAND', 'EARNING', 'ITEMS SOLD', 'PROFIT']
            for row in data:
                table.rows.append(row)
            print(table)

        elif c == 3:
            code = input("Enter the product code to be checked: ")
            print("Product status:-")
            mysql_csr.execute(
                profitquery+f"AND productinfo.ITEM_CODE ='{code}'")
            data = mysql_csr.fetchall()
            table = BeautifulTable()
            table.columns.header = [
                "ITEM_CODE", '   NAME        ', 'BRAND', 'EARNING PER ITEM', 'PROFIT']
            for row in data:
                table.rows.append(row)
            print(table)

        elif c == 4:
            print("Profit chart:-")
            mysql_csr.execute(profitquery)
            data = mysql_csr.fetchall()
            table = BeautifulTable()
            table.columns.header = [
                "ITEM_CODE", '     NAME        ', 'BRAND', 'EARNING PER ITEM', "PROFIT"]
            for row in data:
                table.rows.append(row)
            print(table)

        elif c == 5:
            print("Supplier logs:-")
            mysql_csr.execute(supplierquery)
            data = mysql_csr.fetchall()
            table = BeautifulTable(80)

            table.columns.header = [
                "ITEM_CODE", 'NAME', 'BRAND', "SUPPLIER NAMES", 'TOTAL_PAID_INVESTMENT']
            for row in data:
                table.rows.append(row)
            print(table)

        elif c == 6:
            print("Register Closed!")
            break
        else:
            print("\nWrong input!")
            continue
