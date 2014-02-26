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
    python command.py <DATABASE> section delete <name SECTION-NAME|id SECTION-ID>
    python command.py <DATABASE> section list <name SECTION-NAME|id SECTION-ID> [PAGE=1] [COUNT-PER-PAGE=30]
    python command.py <DATABASE> section post <name SECTION-NAME|id SECTION-ID> <TITLE> <CONTENT> [ARGUMENTS]

    python command.py <DATABASE> topic reply <TOPIC-ID> <CONTENT> [ARGUMENTS]
    python command.py <DATABASE> topic delete <TOPIC-ID>
    python command.py <DATABASE> topic list <TOPIC-ID> [PAGE=1] [COUNT-PER-PAGE=30]
""".strip()

argvProgram = sys.argv[0]
argv = sys.argv[1:]

try:
    dbpath = argv[0]
    mainAction = argv[1]
    if mainAction != 'initialize':
        subAction = argv[2]
        argv = argv[2:]
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
    pass

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
