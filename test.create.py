from  bbs import initDatabase
from sql.sqlite import sqlite

sqldb = sqlite(filename="test.sqlite")

initDatabase(sqldb)

sqldb.close()
