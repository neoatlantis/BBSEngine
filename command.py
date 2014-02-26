# -*- coding: utf-8 -*-
import sys

from bbs import initDatabase
from bbs.topic import topic
from bbs.section import section
from sql.sqlite import sqlite

usage = """
Usage:
    python command.py <DATABASE> initialize

    python command.py <DATABASE> section create <SECTION-NAME>
    python command.py <DATABASE> section delete <SECTION-NAME|SECTION-ID>
    python command.py <DATABASE> section list <SECTION-NAME|SECTION-ID> [PAGE=1] [COUNT-PER-PAGE=30]
    python command.py <DATABASE> section post <SECTION-NAME|SECTION-ID> <TITLE> <CONTENT> [ARGUMENTS]

    python command.py <DATABASE> topic reply <TOPIC-ID> <CONTENT> [ARGUMENTS]
    python command.py <DATABASE> topic delete <TOPIC-ID>
    python command.py <DATABASE> topic list <TOPIC-ID> [PAGE=1] [COUNT-PER-PAGE=30]
""".strip()

argvProgram = sys.argv[0]
argv = sys.argv[1:]

try:
    dbpath = argv[0]
    mainAction = argv[1]
    argv = argv[2:]
    if mainAction != 'initialize':
        subAction = argv[0]
        argv = argv[1:]
except:
    print usage
    sys.exit(1)


sqldb = sqlite(filename="test.sqlite")

################################ INITIALIZE ##################################
if mainAction == 'initialize':
    initDatabase(sqldb)
    sqldb.close()
    sys.exit(0)

################################# SECTION ####################################
if mainAction == 'section':
    try:
        sectionSpec = argv[0]
        argv = argv[1:]
    except:
        print usage
        sys.exit(1)

    thisSection = section(sqldb)

    if subAction == 'create':
        result = thisSection.create(sectionSpec)
        if result == True:
            sys.exit(0)
        else:
            print '! %s' % result
            sys.exit(2)

    ############### FOLLOWING REQUIRES LOADING THIS SECTION ##############

    result = thisSection.load(sectionSpec)
    if True != result:
        print '! %s' % result
        sys.exit(2)

    if subAction == 'delete':
        thisSection.delete()
        sys.exit(0)

    if subAction == 'list':
        page = 1
        perpage = 50
        try:
            page = argv[0]
            perpage = argv[1]
        except:
            pass
        result = thisSection.list(page, perpage)
        if type(result) == list:
            print result
            sys.exit(0)
        else:
            print '! %s' % result
            sys.exit(2)

    if subAction == 'post':
        try:
            title = argv[0]
            content = argv[1]
            argv = argv[2:]
        except:
            print usage
            sys.exit(1)
        thisTopic = thisSection.topic()
        result = thisTopic.create(title, content)
        if type(result) != str:
            print '! %s' % result
            sys.exit(2)
        else:
            print '* %s' % result
            sys.exit(0)


################################## TOPIC #####################################
if mainAction == 'topic':
    try:
        topicID = argv[0]
    except:
        print usage
        sys.exit(1)

    thisTopic = topic(sqldb)
    loadResult = thisTopic.load(topicID)
    if loadResult != True:
        print '! %s' % loadResult 
        sys.exit(2)

    if subAction == 'delete':
        pass

################################### END ######################################
print mainAction
sys.exit(127)
