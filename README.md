BBSEngine
=========

This tiny program aims at implementing a easy of way of interacting with a BBS
system. It includes the necessary logic of a BBS, namely creating, deleting of
`sections`, as well as creating, deleting, replying the `topics`. All logics
are executable via a python script in command line, and it should be fairly
easy to write web-based actual BBS systems interacting with this tool.

Neither user nor authority managements are implemented. They are assumed to be
carried out by external systems. An `argument` field together with each record
of `section` and `topic` is provided and can be used to record such data.
