# linesdir.py
#
# Generate a sequence of lines from files in a directory

from genfind import *
from gencat import *
from genopen import *

def lines_from_dir(filepat, dirname):
    names = gen_find(filepat,dirname)
    files = gen_open(names)
    lines = gen_cat(files)
    return lines

# Example use

if __name__ == '__main__':
    loglines = lines_from_dir("access-log*","www")
    for line in loglines:
        print line,
