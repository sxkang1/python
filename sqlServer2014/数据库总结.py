"""
1、创建数据库连接
    import pymssql
    conn = pymssql.connect(host,user,password,database)
2、声明游标
    cursor = conn.cursor() # 用来执行sql语句，关闭数据库
3、编写SQL语句
    SELECT * FROM persons
    INSERT INTO persons VALUES('No1.','宋小康','男')
    update persons set id=No2. where id=1
    DELETE FROM persons WHERE id=2

4、创建表 persons，包含字段：ID、name、salesrep
    cursor.execute(
        IF OBJECT_ID('persons', 'U') IS NOT NULL
            DROP TABLE persons
        CREATE TABLE persons (
            id INT NOT NULL,
            name VARCHAR(100),
            salesrep VARCHAR(100),
            PRIMARY KEY(id)
        ))
5、执行sql语句，执行一条或者多条数据
    execute(sql语句) executemany(sql语句，数据)
6、提交数据库，增删改才需要提交，查不需要
    conn.commit() # 不是用光标来提交哦 使用数据库提交
7、关闭数据库
    cursor.close()

8、获取一条或多条数据
    fetchone() fetchall()

"""
