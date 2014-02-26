# -*- coding: utf-8 -*-
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
