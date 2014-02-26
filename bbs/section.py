# -*- coding: utf-8 -*-
import hashlib
import re

from _id import _isSectionID, _regulateSectionName, _getSectionID
from topic import topic

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

        self._loadID = section[0]
        self.name = section[1].decode('hex')
        return True

    def existence(self, sectionID):
        sql = "SELECT sid, name FROM sections WHERE sid = '%s'" % sectionID
        queryResult = self._sqldb.fetchOne(sql)
        print sql
        print queryResult
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

        self.load(sectionID)
        return True

    def list(self, page):
        try:
            page = int(page)
        except:
            page = 1
        sql = "SELECT * FROM sections WHERE sid = '%s'" % self._loadID

    def refresh(self):
        pass

    def topic(self):
        if not self._loadID:
            return Exception('section-not-loaded')

        return topic(self._sqldb, self._loadID)
