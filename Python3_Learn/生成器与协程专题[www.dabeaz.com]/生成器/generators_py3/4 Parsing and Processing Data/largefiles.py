# largefiles.py
# 查询所有请求资源字节超过1MB的请求
# Find all transfers over a megabyte

from linesdir import *
from apachelog import *

lines = lines_from_dir("access-log*", "www")
log = apache_log(lines)

large = (r for r in log
         if r['bytes'] > 1024 * 1024)

for r in large:
    print(r['request'], r['bytes'])
