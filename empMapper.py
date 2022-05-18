#!/usr/bin/python
import sys

# input comes from STDIN (standard input)
for line in sys.stdin:

    line = line.strip()
    split = line.split('|')

    if "," in split[3]: #Mapper1, First, Last and Address
            print ("%s\t%s\t%s" % (split[1],split[2],split[3]))
    else:                                                    #Mapper2: First, Last and Extension
            print ("%s\t%s\t%d" % (split[1],split[2],split[3]))
