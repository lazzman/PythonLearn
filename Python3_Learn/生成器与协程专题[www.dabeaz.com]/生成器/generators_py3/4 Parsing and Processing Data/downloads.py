# downloads.py
# 统计指定的资源被下载次数
# Find out how many downloads of a specific request

from linesdir import *
from apachelog import *

lines = lines_from_dir("access-log*", "www")
log = apache_log(lines)

request = 'ply/ply-2.3.tar.gz'

total = sum(1 for r in log
            if r['request'] == '/ply/ply-2.3.tar.gz')

print("Total Download Times：", total)
