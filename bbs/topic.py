# -*- coding: utf-8 -*-

"""
topic:
    tid: TopicID, for this topic.
    pid: parentID, either a sectionID or another TopicID.
         ** baseing on different policies, the parent topic(when pid is of 
         a TopicID), can have its pid only specified to a sectionID, or
         possible also a TopicID. In the first case, this will be rather
         traditional, and in the second case, this will enable direct answers
         to a 'reply'.
    title: only useful when pid is a sectionID.
    content: actual content.
    sid: records the section, to which this topic or its parent belongs to.
         ** this is just for caching.
    arguments: store other necessary values for this entry.
"""

import hashlib
import time

from _id import _isTopicID, _getTopicID, _isSectionID


class topic:
    
    _sqldb = False
    _sectionID = False

    _topicID = False
    
    def __init__(self, sqldb, sectionID):
        self._sqldb = sqldb
        if not _isSectionID(sectionID):
            raise Exception('not-section-id')
        self._sectionID = sectionID

    def create(self, title, content, **argv):
        topicID = _getTopicID(self._sectionID, title, content)

        posttime = int(time.time())
        try:
            if argv.has_key('time'):
                posttime = int(argv['time'])
        except:
            pass

        self._sqldb.insert(
            'topics', 
            {
                'tid': topicID,
                'pid': self._sectionID,
                'title': title.encode('hex'),
                'content': content.encode('hex'),
                'sid': self._sectionID,
                'time': posttime,
            }
        )

        # inform the update of this section
        # TODO

        self.load(topicID)
        return topicID

    def load(self, topicID):
        if not _isTopicID(topicID):
            return Exception('not-topic-id')
        
        sql = 'SELECT tid, sid, content, title FROM topics '\
            + ('WHERE tid = "%s"' % topicID)
        result = self._sqldb.fetchOne(sql)

        if not result:
            return Exception('topic-not-exists')

        self._topicID = result[0] 
        self._sectionID = result[1]
        self.content = result[2].decode('hex')
        self.title = result[3].decode('hex')

        return True 

    def reply(self, content, **argv):
        if not self._topicID:
            return Exception('topic-not-loaded')

        topicID = _getTopicID(self._topicID, '', content)
        posttime = int(time.time())
        try:
            if argv.has_key('time'):
                posttime = int(argv['time'])
        except:
            pass

        self._sqldb.insert(
            'topics', 
            {
                'tid': topicID,
                'pid': self._topicID,
                'title': '',
                'content': content.encode('hex'),
                'sid': self._sectionID,
                'time': posttime,
            }
        )

        return True

    def list(self, page, perpage=30):
        if not self._topicID:
            return Exception('topic-not-loaded')

        try:
            page, prepage = int(page), int(prepage)
        except:
            page, prepage = 1, 30

        sql = "SELECT tid, title, content FROM topics WHERE "\
            + ("pid = '%s' ORDER BY time DESC " % self._topicID)\
            + ("LIMIT %d OFFSET %d" % (perpage, (page - 1) * perpage))

        result = self._sqldb.fetchMore(sql)
        return result
