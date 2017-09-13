# hosts.py
#
# Find unique host IP addresses

from linesdir import *
from apachelog import *

lines = lines_from_dir("access-log*","www")
log = apache_log(lines)

hosts = set(r['host'] for r in log)
for h in hosts:
    print h
