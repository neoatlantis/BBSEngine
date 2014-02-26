# -*- coding: utf-8 -*-

def initDatabase(sqldb):
    sqls = [
        """
            CREATE TABLE "main"."sections" (
                "sid" TEXT NOT NULL,
                "alias" TEXT,
                "name" TEXT,
                "arguments" TEXT
            );
        """,
        """
            CREATE TABLE "main"."topics" (
                "tid" TEXT NOT NULL,
                "pid" TEXT,
                "title" TEXT,
                "content" TEXT,
                "sid" TEXT,
                "arguments" TEXT
            );
        """,
    ]

    for each in sqls:
        sqldb.execute(each)
