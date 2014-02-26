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

        self._sqldb.insert(
            'topics', 
            {
                'tid': topicID,
                'pid': self._sectionID,
                'title': title.encode('hex'),
                'content': content.encode('hex'),
                'sid': self._sectionID,
            }
        )

        # inform the update of this section
        # TODO

        print self._sqldb.fetchOne('SELECT * FROM topics')

        self.load(topicID)
        return topicID

    def load(self, topicID):
        if not _isTopicID(topicID):
            return Exception('not-topic-id')

        self._topicID = topicID

    def reply(self, content, **argv):
        if not self._topicID:
            return Exception('topic-not-loaded')
