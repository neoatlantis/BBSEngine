from  bbs.section import section
from sql.sqlite import sqlite

sqldb = sqlite(filename="test.sqlite")

s = section(sqldb)
print s.load('test')
print s.create('test')

sqldb.close()
