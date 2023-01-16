import mysql.connector as msql
import pickle


inp = input("Mysql password: ")
entr_pass = str(inp)

# Connecting to the database
ms = msql.connect(host='localhost', user='root',
                    passwd=entr_pass)

if ms.is_connected():
    print("\nWelcome!")
else:
    print("Failed to connect to database!")
mysql_csr = ms.cursor()
mysql_csr.execute("create database if not exists pyth")
ms.commit()
mysql_csr.execute("use pyth")
ms.commit()
mysql_csr.execute("show tables")
c = mysql_csr.fetchall()
if len(c) != 5:
    import os
    cwd = (__file__.replace(os.path.basename(__file__),"")).removesuffix("modules\\") + "database.sql"
    mysql_csr.execute(f"source {cwd}")
    ms.commit()
