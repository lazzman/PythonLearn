# largest.py
# 查找传输最大的请求信息
# Find the largest file

from linesdir import *
from apachelog import *

lines = lines_from_dir("access-log*", "www")
log = apache_log(lines)

print("%d %s" % max((r['bytes'], r['request'])
                    for r in log))
