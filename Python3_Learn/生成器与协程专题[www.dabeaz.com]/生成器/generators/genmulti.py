# genmulti.py
#
# Generate items from multiple generators (multiplex)
#

import Queue, threading
def gen_multiplex(genlist):
    item_q = Queue.Queue()
    def run_one(source):
        for item in source: item_q.put(item)

    def run_all():
        thrlist = []
        for source in genlist:
            t = threading.Thread(target=run_one,args=(source,))
            t.start()
            thrlist.append(t)
        for t in thrlist: t.join()
        item_q.put(StopIteration)

    threading.Thread(target=run_all).start()
    while True:
        item = item_q.get()
        if item is StopIteration: return
        yield item


# Example use
#
# This example requires you to perform these setup steps:
#
# 1.  Go to run/foo and run logsim.py
# 2.  Go to run/bar and run logsim.py
#
# These two steps will start writing two different Apache log files.
# Now, we're going to read from both at the same time.

if __name__ == '__main__':
    from follow import *
    
    log1 = follow(open("run/foo/access-log"))
    log2 = follow(open("run/bar/access-log"))
    
    log = gen_multiplex([log1,log2])
    
    for line in log:
        print line,
