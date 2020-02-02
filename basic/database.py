# import mysql.connector
#
# my_db=mysql.connector.connect(
#     host='127.0.0.1',
#     user='root',
#     password='',
#
# )
#
# print(my_db)
#
#
# import mysql.connector
# try:
#
#     my_db = mysql.connector.connect(
#         hostt='127.0.0.1',
#         user='root',
#         password='',
#
#     )
# except Exception as e:
#     print(e)

# import mysql.connector
# # ========connection========
#
# my_db=mysql.connector.connect(
#     host='127.0.0.1',
#     user='root',
#     password='',
#     database='python7amnew'
#
# )
#
# my_cursor=my_db.cursor()
# # =======query for create database =======
#
# query="CREATE DATABASE IF NOT EXISTS python7amnew"
#
# my_cursor.execute(query)
#
# create_query="CREATE TABLE IF NOT EXISTS users(id int AUTO_INCREMENT PRIMARY KEY, name varchar(100))"
#
# my_cursor.execute(create_query)
#
# insert_query="INSERT INTO users(name)VALUES('hari')"
# my_cursor.execute(insert_query)
# my_db.commit()

# delete_query="DELETE FROM `users` WHERE id=2"
# my_cursor.execute(delete_query)
# my_db.commit()

# select_query="SELECT * FROM users"
# my_cursor.execute(select_query)
#
# result=my_cursor.fetchall()
# # result=my_cursor.fetchone() """fetches only one data"""
# # result=my_cursor.fetchmany() """fetches data as per our requirement"""
# for user in result:
#     print(user)
#
#
# my_cursor=''
#
# def db_connection():
#     global my_cursor
#     pass
#
# def insert(tablename, **data):
#     print(data)

# insert('users', name='ram', age=20)

