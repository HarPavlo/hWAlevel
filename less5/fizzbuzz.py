def fizzbuzz(f, b, n):
    lst = []
    for i in range(1, n + 1):
        if i % f == 0 and i % b == 0:
            i = "FB"
        elif i % f == 0:
            i = "F"
        elif i % b == 0:
            i = "B"
        else:
            i = str(i)
        lst.append(i)
    return "".join(lst) + "\n"


filename = "C:\\Users\PVNT\PycharmProjects\pythonProject\less5\\fizzbuzz.txt"
filename2 = "C:\\Users\PVNT\PycharmProjects\pythonProject\less5\\fizzbuzzresult.txt"

f = open(filename)
f2 = open(filename2, "w")

for i in f:
    a, b, c = map(int, i.split())
    f2.write(fizzbuzz(a, b, c))
f.close()
f2.close()
