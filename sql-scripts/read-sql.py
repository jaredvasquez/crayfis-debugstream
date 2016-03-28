#!/usr/bin/python

import MySQLdb

# Open database connection
db = MySQLdb.connect("localhost","debug","test123","test" )

# prepare a cursor object using cursor() method
cursor = db.cursor()

# Prepare SQL query to INSERT a record into the database.
sql = "SELECT * FROM STATUS"

try:
    # Execute the SQL command
    cursor.execute(sql)
    # Fetch all the rows in a list of lists.
    results = cursor.fetchall()
    for row in results:
        print row
except:
    print "Error: unable to fecth data"

# disconnect from server
db.close()
