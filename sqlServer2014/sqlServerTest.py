import pymssql

conn = pymssql.connect(host='.', user='sa', password='root', database='TestSqlServer')
cursor = conn.cursor()
print(cursor)
# 创建 表 结构
cursor.execute("""
IF OBJECT_ID('testTable1', 'U') IS NOT NULL
    DROP TABLE testTable1
CREATE TABLE testTable1 (
    id INT NOT NULL,
    name VARCHAR(100),
    age VARCHAR(100),
    PRIMARY KEY(id)
)
""")
# 添加一条数据
sql_insert = "INSERT INTO testTable1 VALUES(1, '张三', 18)"
cursor.execute(sql_insert)
conn.commit()



cursor.close()

