import pymssql

conn = pymssql.connect(host='.', user='sa', password='root', database='TestSqlServer')
cursor = conn.cursor()
print(111)
# 创建 表 结构
# cursor.execute("""
# IF OBJECT_ID('testTable2', 'U') IS NOT NULL
#     DROP TABLE testTable2
# CREATE TABLE testTable2 (
#     id INT NOT NULL,
#     name VARCHAR(100),
#     age VARCHAR(100),
#     PRIMARY KEY(id)
# )
# """)
#
# # 插入三条测试数据
# cursor.executemany(
#     "INSERT INTO testTable1 VALUES (%d, %s, %s)",
#     [(1, '宋小康', '27'),
#      (2, '丁文超', '24'),
#      (3, '张建', '25')])
# conn.commit()
# cursor.close()