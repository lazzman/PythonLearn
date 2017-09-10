# genfind.py
#
# A function that generates files that match a given filename pattern

import os
import fnmatch

def gen_find(filepat,top):
    for path, dirlist, filelist in os.walk(top):
        for name in fnmatch.filter(filelist,filepat):
            yield os.path.join(path,name)

# Example use

if __name__ == '__main__':
    lognames = gen_find("access-log*","www")
    for name in lognames:
        print name
