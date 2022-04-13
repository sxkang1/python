import pymssql

connect = pymssql.connect(host='.', user='sa', password='root', database='tempdb')
cursor = connect.cursor()

execute = "DELETE FROM persons WHERE id = 4 "
cursor.execute(execute)
connect.commit()
cursor.close()
