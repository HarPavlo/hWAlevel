# numb = int(input("Enter a number: "))
# if numb >= 0 and numb % 3:
#     print("YES!")
# else:
#     print("Try again")
#
# numb = int(input("Enter a number: "))
# if numb > 0:
#     print("positive number")
# elif numb == 0:
#     print("Zero")
# else:
#     print("negative number")
#
# numb = int(input("Enter a number: "))
# if not numb % 2 or not numb % 5:
#     print(numb)

fizz = int(input("Enter a number fizz: "))
buzz = int(input("Enter a number buzz: "))
numb = int(input("Enter a number: "))

for i in range(1, numb + 1):
    if i % fizz == 0 and i % buzz == 0:
        i = "FB"
    elif i % fizz == 0:
        i = "F"
    elif i % buzz == 0:
        i = "B"
    else:
        i = i
    print(i, end=" ")
