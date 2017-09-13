# gengrep.py
#
# Grep a sequence of lines that match a re pattern

import re
def gen_grep(pat,lines):
    patc = re.compile(pat)
    for line in lines:
        if patc.search(line): yield line

# Example use

if __name__ == '__main__':
    from genfind import  gen_find
    from genopen import  gen_open
    from gencat  import  gen_cat

    lognames = gen_find("access-log*","www")
    logfiles = gen_open(lognames)
    loglines = gen_cat(logfiles)

    # Look for ply downloads (PLY is my own Python package)
    plylines = gen_grep(r'ply-.*\.gz',loglines)
    for line in plylines:
        print line,
