import pymssql

connect = pymssql.connect(host='.', user='sa', password='root', database='tempdb', charset='utf8')
cursor = connect.cursor()  # 游走的光标

# 插入sql语句 insert into persons values
sql_insert = "INSERT INTO persons VALUES(%d,'宋小康2','康康2')" % int(5)

try:
    cursor.execute(sql_insert)  # 执行sql语句
    connect.commit()  # 提交数据库
    cursor.close()
except:
    cursor.close()  # 利用光标关闭数据库
