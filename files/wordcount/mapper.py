#!/usr/bin/env python3

import sys

for input_line in sys.stdin:
    input_line = input_line.strip()
    keys = input_line.split()
    for key in keys:
        value = 1
        print('%s\t%d' % (key, value))
