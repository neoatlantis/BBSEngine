# -*- coding: utf-8 -*-

def initDatabase(sqldb):
    sqls = [
        """
            CREATE TABLE "main"."sections" (
                "sid" TEXT NOT NULL,
                "name" TEXT,
                "arguments" TEXT
            );
        """,
    ]

    for each in sqls:
        sqldb.execute(each)
