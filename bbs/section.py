# -*- coding: utf-8 -*-
import hashlib
import re

def _getSectionID(sectionNameOrID):
    if re.match('^\\$[0-9a-f]{32}$', sectionNameOrID):
        return sectionNameOrID
    else:
        digest = hashlib.sha1(sectionNameOrID.strip().lower()).hexdigest()
        return '$' + digest[:32]

##############################################################################

class section:

    _loadID = False
    _sqldb = False
    
    def __init__(self, sqldb):
        self._sqldb = sqldb

    def load(self, sectionNameOrID):
        wantedID = _getSectionID(sectionNameOrID)
        # TODO alias
        sql = "SELECT * FROM sections WHERE sid = '%s'" % wantedID

        queryResult = self._sqldb.fetchOne(sql)
        
        if not queryResult:
            return Exception('section-not-exists')

        


    def list(self, page):
        pass

    def refresh(self):
        pass
