# query404.py
# 打印全部日志中404的请求资源
# Find the set of all documents that 404 in a log file

from linesdir import *
from apachelog import *

lines = lines_from_dir("access-log*", "www")
log = apache_log(lines)

stat404 = set(r['request'] for r in log
              if r['status'] == 404)

for r in sorted(stat404):
    print(r)
