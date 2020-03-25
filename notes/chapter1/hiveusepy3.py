from impala.dbapi import connect

conn = connect(host='132.232.58.47',port=10000,database='default',auth_mechanism='LDAP',user='hive',password='hive@Tbds.com')
print (type(conn))

cur = conn.cursor()

sql = "select * from dbdemo.tbdemo"

cur.execute(sql)

print(cur.fetchall())

