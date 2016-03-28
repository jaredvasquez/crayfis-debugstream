#!/usr/bin/python

import MySQLdb

# Open database connection
db = MySQLdb.connect("localhost","debug","test123","test" )

# prepare a cursor object using cursor() method
cursor = db.cursor()

# Drop table if it already exist using execute() method.
cursor.execute("DROP TABLE IF EXISTS STATUS")

# Create table as per requirement
sql = """CREATE TABLE STATUS (
         PHONE_ID CHAR(16) NOT NULL,
         PHONE_DESC VARCHAR(24),
         LAST_UPDATED VARCHAR(30),
         NXBS INT,
         EVENTS INT,
         L1THRESH INT,
         FPS FLOAT )"""

cursor.execute(sql)

# disconnect from server
db.close()
