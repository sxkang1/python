import pymssql

host = '.'
user = 'sa'
password = 'root'
database = ''
charset = 'utf8'
# 打开数据库连接
conn = pymssql.connect(host, user, password, "tempdb")  # 指定数据库'tempdb'
cursor = conn.cursor()  # 游走光标

sql_select = "SELECT * FROM persons"

sql_insert = "INSERT INTO persons VALUES('No1.','宋小康','男')"

sql_update = "update persons set id=No2. where id=1"

sql_delete = "DELETE FROM persons WHERE id=2"

# 创建表 persons，包含字段：ID、name、salesrep
cursor.execute("""
IF OBJECT_ID('persons', 'U') IS NOT NULL
    DROP TABLE persons
CREATE TABLE persons (
    id INT NOT NULL,
    name VARCHAR(100),
    salesrep VARCHAR(100),
    PRIMARY KEY(id)
)
""")
# 插入三条测试数据
cursor.executemany(
    "INSERT INTO persons VALUES (%d, %s, %s)",
    [(1, 'John Smith', 'John Doe'),
     (2, 'Jane Doe', 'Joe Dog'),
     (3, 'Mike T.', 'Sarah H.')])

# 如果连接时没有设置autocommit为True的话，必须主动调用commit() 来保存更改。
conn.commit()


# 查询一条匹配数据
cursor.execute('SELECT * FROM persons WHERE salesrep=%s', 'John Doe')
# 获取一条记录 fetchone
row = cursor.fetchone()

# 查询所有数据 fetchall
cursor.execute(sql_select) # 执行sql语句
results = cursor.fetchall() # 获取所有数据
print(results)

# 循环打印记录(这里只有一条，所以只打印出一条)
for result in results:
    print("ID=%d, Name=%s, salesrep=%s" % (result[0], result[1], result[2]))
    row = cursor.fetchone()
# 连接用完后记得关闭以释放资源
conn.close()
