# genshutdown.py
# 关闭生成器
# Example of shutting down a generator
#
# Requires you to run run/foo/logsim.py to get a real-time source

from follow import *

lines = follow(open("access-log"))
for i, line in enumerate(lines):
    print(line, )
    if i == 10:
        # 关闭生成器
        lines.close()
