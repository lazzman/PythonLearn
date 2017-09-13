# 本demo用于制作大型的访问日志文件以便于后面进行性能测试

# 文件目录下打开控制台输入：python makebig.py 10 会在当前目录下生成一个6M+的日志文件

import sys

if len(sys.argv) != 2:
    print("运行方法 : makebig.py 重复次数", file=sys.stderr)
    raise SystemExit(1)

data = open("access-log").read()

f = open("big-access-log", "w")
for i in range(int(sys.argv[1])):
    f.write(data)
