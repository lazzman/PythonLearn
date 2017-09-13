# storelast.py
#
# An iterator that stores the last value returned.  

class storelast(object):
    def __init__(self,source):
        self.source = source
    def next(self):
        item = self.source.next()
        self.last = item
        return item
    def __iter__(self):
        return self

# Example
if __name__ == '__main__':
    from follow import *
    from apachelog import *

    lines = storelast(follow(open("run/foo/access-log")))
    log   = apache_log(lines)

    for r in log:
        print r
        print lines.last
