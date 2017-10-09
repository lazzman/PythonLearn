# robots.py
# 查询哪些主机爬取了当前网站(访问robots.txt)
# Find out who has been hitting robots.txt

from linesdir import *
from apachelog import *

lines = lines_from_dir("access-log*", "www")
log = apache_log(lines)

addrs = set(r['host'] for r in log
            if 'robots.txt' in r['request'])

import socket

for addr in addrs:
    try:
        # 根据ip地址反向查找主机名称
        print(socket.gethostbyaddr(addr)[0])
    except socket.herror:
        print(addr)
