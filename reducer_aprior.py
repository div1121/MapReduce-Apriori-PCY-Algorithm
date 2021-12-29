#!/usr/bin/env python
"""reducer.py"""

import sys

# input comes from STDIN
for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip()
    # parse the input we got from mapper.py
    key, value = line.split('\t', 1)
    print "%s" %(key)
