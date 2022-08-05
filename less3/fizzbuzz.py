import sys
lst = []
filename = sys.argv[1]
f = open(filename, 'r')
filename1 = sys.argv[2]
f1 = open(filename1, 'w')
for line in f:
    line = line.split()
    lst = []
    for i in range(1, int(line[2]) + 1):
        if i % int(line[0]) == 0 and i % int(line[1]) == 0:
            i = "FB"
        elif i % int(line[0]) == 0:
            i = "F"
        elif i % int(line[1]) == 0:
            i = "B"
        else:
            i = i
        lst.append(i)
    lst = "".join(map(str, lst))
    f1.write(lst + '\n')
f1.close()
f.close()
