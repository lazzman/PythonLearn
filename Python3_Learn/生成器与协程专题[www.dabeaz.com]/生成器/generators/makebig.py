# Make a big log file for testing

import sys

if len(sys.argv) != 2:
    print >>sys.stderr,"Usage : makebig.py repetitions"
    raise SystemExit(1)

data = open("access-log").read()

f = open("big-access-log","w")
for i in xrange(int(sys.argv[1])):
    f.write(data)



    
