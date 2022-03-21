import os
import psycopg2

conn = psycopg2.connect(
        host="localhost",
        database="flask_eyesight",
        user=os.environ['DB_USERNAME'],
        password=os.environ['DB_PASSWORD'])

# Open a cursor to perform database operations
cur = conn.cursor()

# Execute a command: this creates a new table
cur.execute('DROP TABLE IF EXISTS users;')
cur.execute('CREATE TABLE users (userID serial PRIMARY KEY,'
                                 'username varchar (150) NOT NULL,'
                                 'password varchar (250) NOT NULL);'
				)
cur.execute('DROP TABLE IF EXISTS objects;')
cur.execute('CREATE TABLE objects (objects_id SERIAL,'
				   'objet_1 varchar (50),'
				   'objet_2 varchar (50),'
				   'objet_3 varchar (50),'
				   'objet_4 varchar (50),'
				   'objet_5 varchar (50),' 
				   'objet_6 varchar (50),'
				   'user_id integer REFERENCES users);'
				   )

# Insert data into the table

conn.commit()

cur.close()
conn.close()

