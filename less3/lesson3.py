# L = list(range(10))
# sum1 = sum2 = 0
# for i in L:
#     sum1 += i
# print(sum1)
#
# i = 0
# while i < len(L):
#     sum2 += i
#     i += 1
# print(sum2)

# # the program output itself
# import sys
#
# filename = sys.argv[0]
# f = open(filename, 'r')
# for line in f:
#     print(line)
# f.close()


# # file output backwards line by line
# import sys
#
# filename = sys.argv[1]
# f = open(filename, 'r')
# for line in f:
#     print(line[::-1])
# f.close()


# file output backwards
import sys

filename = sys.argv[1]
f = open(filename, 'r')
print(f.read()[::-1])
f.close()
