import mysql.connector

conn = mysql.connector.Connect(host="localhost",username="root",password="1234h", database="test_pycham2")
my_cur = conn.cursor()

Query = "SELECT * FROM customers WHERE S_Name ='MJ,Jalgaon'"

my_cur.execute(Query)

records = my_cur.fetchall()
for x in records:
  print(x)
