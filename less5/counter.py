import re
import sys


def punctuation(j):
    return re.sub(r'[!?.:;,"()-]', "", j)


def counter(i):
    if i in fl:
        g = fl.count(i)
        return str(g) + "=>" + i


filename = sys.argv[1]
filename2 = sys.argv[2]
f = open(filename)
f2 = open(filename2, 'w')

fl = sum(list(map(str.split, f)), [])
fl = list(map(lambda y: punctuation(y).lower(), fl))
fs = set(fl)
fs = list(map(str.lower, fs))
f2.write("\n".join(list(map(lambda x: counter(x), fs))))

f.close()
f2.close()
