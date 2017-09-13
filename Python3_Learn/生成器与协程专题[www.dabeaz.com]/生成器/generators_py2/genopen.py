# genopen.py
#
# Takes a sequence of filenames as input and yields a sequence of file
# objects that have been suitably open

import gzip, bz2

def gen_open(filenames):
    for name in filenames:
        if name.endswith(".gz"):
            yield gzip.open(name)
        elif name.endswith(".bz2"):
            yield bz2.BZ2File(name)
        else:
            yield open(name)

# Example use

if __name__ == '__main__':
    from genfind import  gen_find
    lognames = gen_find("access-log*","www")
    logfiles = gen_open(lognames)
    for f in logfiles:
        print f
