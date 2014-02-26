from  bbs.section import section
from sql.sqlite import sqlite

sqldb = sqlite(filename="test.sqlite")

s = section(sqldb)

if True != s.load('test'):
    print '***** Create Section *****'
    print s.create('test')

print s.name

topic = s.topic()

topicList = s.list(1)
firstID = topicList[0]['tid']

print topic.load(firstID)

#print '***** reply to this topic *****'
#print topic.reply('Hallo!')

print '-----'
print topic.list(1)

sqldb.close()
