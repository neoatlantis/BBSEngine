import sqlite3

class sqlite:
    
    _dbfile = False
    _con = False
    
    def __init__(self, **argv):
        self._dbfile = argv.filename
        self._con = sqlite3.connect(self._dbfile)

    def fetchOne(self, sql):
        cursor = self._con.cursor()
        cursor.execute(sql)
        result = cursor.fetchone()
        cursor.close()
        return result
