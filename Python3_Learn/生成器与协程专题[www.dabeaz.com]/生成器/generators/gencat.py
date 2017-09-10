# gencat.py
#
# Concatenate multiple generators into a single sequence

def gen_cat(sources):
    for s in sources:
        for item in s:
            yield item

# Example use

if __name__ == '__main__':
    from genfind import  gen_find
    from genopen import  gen_open

    lognames = gen_find("access-log*","www")
    logfiles = gen_open(lognames)
    loglines = gen_cat(logfiles)
    for line in loglines:
        print line,
