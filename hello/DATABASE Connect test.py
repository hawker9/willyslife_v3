import os
import psycopg2

DATABASE_URL = os.environ['DATABASE_URL']
conn = psycopg2.connect(DATABASE_URL, sslmode='require')

#Creating a cursor object using the cursor() method
cursor = conn.cursor()

#Creating table as per requirement
sql2 = '''INSERT INTO votes (name) VALUES ('TEST');'''


cursor.execute(sql2)

print("Table created successfully........")

#Closing the connection
conn.close()