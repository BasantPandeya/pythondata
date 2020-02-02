# use function to create table, insert data,
# user must ask to delete

import mysql.connector

my_db=mysql.connector.connect(
    host='127.0.0.1',
    user='root',
    password='',
    database='python7amnew'
)
db=my_db.cursor()

def create_table():
    db.execute('CREATE TABLE IF NOT EXISTS newhw(sn REAL, name TEXT, address TEXT, phone REAL)')

def data_entry():
    db.execute("INSERT INTO newhw VALUES(1, 'ram', 'thapagaun', 9844)")
    my_db.commit()
    db.close()
    my_db.close()

create_table()
data_entry()
