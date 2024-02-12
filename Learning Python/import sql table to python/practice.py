import mysql.connector as connection
from mysql.connector import errorcode
import pandas as pd
import os
from datetime import datetime

# Connect to database
try:
    db = connection.connect(user='root', password='Chong1374654%', host='localhost', database='music')
except connection.Error as Error:
    if Error.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("Something is wrong with your user name or password")
    elif Error.errno == errorcode.ER_BAD_DB_ERROR:
        print("Database does not exist")
    else:
        print(Error)

#SQL query
query = 'SELECT * FROM ALBUMS;'

#Importing the sql table to a pandas dataframe for us to manipulate
albums = pd.read_sql(query, db)
