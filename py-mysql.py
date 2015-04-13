#encoding:utf-8

import MySQLdb

db = MySQLdb.connect("localhost","allen","allen","testfo")

cursor = db.cursor()

cursor.execute("SELECT VERSION()")
data = cursor.fetchone()

print "Database version : %s " %data

#cursor.execute("DROP TABLE IF EXISTS EMPLOYEE")

# sql = """CREATE TABLE EMPLOYEE(
# 		FIRST_NAME VARCHAR(20) NOT NULL,
# 		LAST_NAME VARCHAR(20),
# 		AGE INT,
# 		SEX CHAR(1),
# 		IMCOME FLOAT
# 			)"""
# cursor.execute(sql)

sql_insert = """INSERT INTO EMPLOYEE(
				FIRST_NAME,LAST_NAME,AGE,SEX,INCOME)
				VALUES ('Mac','Zhang','21','M',2000)"""
try:
	#执行SQLyuj
	cursor.execute(sql_insert)
	#提交到数据库执行
	db.commit();

except:
	#出错时回滚
	db.rollback()
#关闭数据库链接
db.close()