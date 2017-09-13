# largest.py
#
# Find the largest file

from linesdir import *
from apachelog import *

lines = lines_from_dir("access-log*","www")
log = apache_log(lines)

print "%d %s" % max((r['bytes'],r['request'])
                    for r in log)
