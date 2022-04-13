import pymssql

connect = pymssql.connect(host='.', user='sa', password='root', database='tempdb')
cursor = connect.cursor()

execute = "update persons set salesrep='小红2' where id = 6 "
cursor.execute(execute)
connect.commit()
cursor.close()