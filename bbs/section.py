# -*- coding: utf-8 -*-
import hashlib
import re

def _isSectionID(test):
    if re.match('^\\$[0-9a-f]{32}$', test):
        return True
    return False

def _regulateSectionName(sectionName):
    return sectionName.strip().lower()

def _getSectionID(sectionNameOrID):
    if _isSectionID(sectionNameOrID):
        return sectionNameOrID
    else:
        regulated = _regulateSectionName(sectionNameOrID)
        digest = hashlib.sha1(regulated).hexdigest()
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
       
        section = self.existence(wantedID)
        if False == section:
            return Exception('section-not-exists')

    def existence(self, sectionID):
        sql = "SELECT * FROM sections WHERE sid = '%s'" % sectionID
        queryResult = self._sqldb.fetchOne(sql)
        if not queryResult:
            return False
        return queryResult

    def create(self, sectionName):
        if _isSectionID(sectionName):
            # a sectionName, which looks like a sectionID, is forbidden.
            return Exception('not-section-name')

        # use HEX encode, making it able to search
        sectionNameEncoded = _regulateSectionName(sectionName).encode('hex')
        sectionID = _getSectionID(sectionName)

        if False != self.existence(sectionID):
            return Exception('section-already-exists')

        self._sqldb.insert(
            'sections',
            {
                'sid': sectionID,
                'name': sectionNameEncoded,
            }
        )

    def list(self, page):
        pass

    def refresh(self):
        pass
