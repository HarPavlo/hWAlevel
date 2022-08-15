a = "level"
b = [10, 20, 30]
c = [3, 9, 27, 81, 243, 729]
lst = [a, b, c]
sort = sorted(lst, key=len)
for i in range(0, len(sort[0])):
    myzip = (a[i], b[i], c[i])
    print(myzip)


a = "level"
b = [10, 20, 30]
c = [3, 9, 27, 81, 243, 729]
sort = sorted([a, b, c], key=len)
print([(a[i], b[i], c[i]) for i in range(0, len(sort[0]))])
