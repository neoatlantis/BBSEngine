import sqlite3

class sqlite:
    
    _dbfile = False
    _con = False
    
    def __init__(self, **argv):
        self._dbfile = argv['filename']
        self._con = sqlite3.connect(self._dbfile)

    def close(self):
        self._con.close()
        return

    def fetchOne(self, sql):
        cursor = self._con.cursor()
        cursor.execute(sql)
        result = cursor.fetchone()
        cursor.close()
        return result

    def execute(self, sql):
        cursor = self._con.cursor()
        cursor.execute(sql)
        cursor.close()
        return

    def insert(self, table, kvs):
        keys = ", ".join(['%s' % i for i in kvs.keys()])
        values = ", ".join(['"%s"' % i for i in kvs.values()])
        sql = "INSERT INTO %s(%s) VALUES(%s)" % (table, keys, values)
        self.execute(sql)
        self._con.commit()
        return
