# _*_ coding: utf-8 _*_
import mysql.connector
conn = mysql.connector.connect(user='root', password='root', database='map_reduce')
cursor = conn.cursor()

cursor.execute('create table user (id varchar(20) primary key, name varchar(20))')
cursor.execute('insert into user (id, name) values (%s, %s)', ['1', 'Bob'])
print(cursor.rowcount)
conn.commit()

cursor.execute('select * from user where id=%s', ('1',))
values = cursor.fetchall()
print(values)
cursor.close()
conn.close()