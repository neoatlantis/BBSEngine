# -*- coding: utf-8 -*-
import time

from _id import _isSectionID, _regulateSectionName, _getSectionID
from topic import topic

##############################################################################

class section:

    _loadID = False
    _sqldb = False
    
    def __init__(self, sqldb):
        self._sqldb = sqldb

    def delete(self):
        if not self._loadID:
            return Exception('section-not-loaded')

        _sqldb.execute('DELETE FROM sections WHERE sid = "%s"' % self._loadID)
        self._loadID = False
        return

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

    def list(self, page, perpage=50):
        if not self._loadID:
            return Exception('section-not-loaded')

        try:
            page, prepage = int(page), int(prepage)
        except:
            page, prepage = 1, 50

        """
        # caching

        sql = "SELECT lastUpdate FROM sections WHERE sid = '%s'" % \
            self._loadID

        sectionQuery = self._sqldb.fetchOne(sql)
        try:
            lastUpdate = int(sectionQuery[0])
        except:
            lastUpdate = 0

        nowtime = int(time.time())
        """

        sql = "SELECT tid, title, content, time FROM topics WHERE "\
            + ("pid = '%s' ORDER BY time DESC " % self._loadID)\
            + ("LIMIT %d OFFSET %d" % (perpage, (page - 1) * perpage))

        result = self._sqldb.fetchMore(sql)
        result = [\
            {
                'tid': each[0],
                'title': each[1].decode('hex'),
                'content': each[2].decode('hex'),
                'time': each[3],
            }
            for each in result
        ]
        return result

    def refresh(self):
        pass

    def topic(self):
        if not self._loadID:
            return Exception('section-not-loaded')

        return topic(self._sqldb, self._loadID)
