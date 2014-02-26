# -*- coding: utf-8 -*-
import hashlib
import re

from _id import _isSectionID, _regulateSectionName, _getSectionID

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
