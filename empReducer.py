
#!/usr/bin/python

import sys

# Several print statements are commented out for troubleshooting purposes.
currentKey = None
valsEmp = None
valsCust = None
TotalCount = 0
# print('hi i ran')
# input comes from STDIN
for line in sys.stdin:
  #  print('for statement starts')
    split = line.strip().split('\t')    # strip the strings between tabs
    if isinstance(split, basestring) : # if split is a string
#       print('I am here')
        key = (split[0]+' '+split[1]) #set the key to First " " Last
        value = '\t'.join(split[2])  #set the value to either address or extension

    if currentKey == key: # Same key
        if ',' in value: #if it's an address
#           print('made it')
            valsCust.append(value) #append the address to value
            print(valsCust) #print out the full data
        if ',' not in value: #if it's not an address
            valsEmp.append(value) #append extension to value
            print(valsEmp) #print out the full data
        else:
           print('nothing found')
    else:
       print('really nothing')
