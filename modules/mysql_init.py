import mysql.connector as msql
import pickle
# gathering login information
'''info = open("Backend/login_info.dat", "rb")
a = pickle.load(info)
info.close()'''
inp=input("Mysql password: ")
entr_pass = str(inp)

# Connecting to the database
ms = msql.connect(host='localhost', user='root',passwd=entr_pass, database='Python')
if ms.is_connected():
    print("\nWelcome!")
else:
    print("Failed to connect to database!")
mysql_csr = ms.cursor()
