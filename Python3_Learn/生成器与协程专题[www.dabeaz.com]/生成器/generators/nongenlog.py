# nongenlog.py
#
# Sum up the number of bytes transferred in an Apache log file
# using a simple for-loop.   We're not using generators here.

wwwlog = open("access-log")
total = 0
for line in wwwlog:
    bytestr = line.rsplit(None,1)[1]
    if bytestr != '-':
        total += int(bytestr)

print "Total", total
