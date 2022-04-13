import pymssql

host = '.'
user = 'sa'
password = 'root'
connect = pymssql.connect(host, user, password, 'tempdb')  # 数据库名 tempdb

cursor = connect.cursor()
print(cursor)

# 查询 表：persons  匹配一条数据
cursor.execute("SELECT * FROM persons WHERE id=%d" % int(3))
row = cursor.fetchone()
print('结果：', row)

# sql查询语句 获取该表persons所有数据
sql_select = "SELECT * FROM persons"
cursor.execute(sql_select)  # 光标 执行sql语句
results = cursor.fetchall()  # 获取所有数据
print(results)

cursor.close()
