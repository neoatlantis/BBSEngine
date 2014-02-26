# -*- coding: utf-8 -*-
import hashlib
import re

def _isTopicID(test):
    if re.match('^\\$[0-9a-f]{40}$', test):
        return True
    return False

def _getTopicID(parentID, title, content):
    titleDigest = hashlib.md5(title).hexdigest()
    contentDigest = hashlib.sha256(content).hexdigest()
    joined = "$".join([parentID, titleDigest, contentDigest])
    
    digest = hashlib.sha1(joined).hexdigest()
    return '$' + digest[:40]

##############################################################################

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
