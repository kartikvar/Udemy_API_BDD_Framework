import cx_Oracle
# through terminal, pip install cx-Oracle
import mysql.connector
# through terminal, pip install mysql-connector-python

from utilities.configurations import *

conn = getConnection()
cursor = conn.cursor()
cursor.execute("select * from ipcs_price where partid=1 and locid=1")

row = cursor.fetchall()
