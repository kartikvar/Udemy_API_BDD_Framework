import cx_Oracle
# through terminal, pip install cx-Oracle
import mysql.connector
# through terminal, pip install mysql-connector-python
'''
database = mysql.connector.connect(
    host="localhost",
    user="sa",
    password="Password02",
    database="Engine13010"
)
'''
con = cx_Oracle.connect('SPPSWAF/SPPSWAF@andcsv-devdb16d:1521/sa')
#cursor = database.cursor()
cursor = con.cursor()
cursor.execute("select * from ipcs_price where partid=1 and locid=1")

for i in cursor:
    print(i)
    print("Standard Price is --> ", i[4])
