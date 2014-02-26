from  bbs.section import section
from sql.sqlite import sqlite

sqldb = sqlite(filename="test.sqlite")

s = section(sqldb)

if True != s.load('test'):
    print '***** Create Section *****'
    print s.create('test')

print s.name

topic = s.topic()
#topic.create('first topic', 'content')

print s.list(1)

sqldb.close()
