number = int(input("write the number: "))
if number % 2:
    print("odd")
else:
    print("even")

number = int(input("write the number: "))
if number % 2 and not number % 3 and not number % 5 and number % 10:
    print(number)

number = int(input("write the number: "))
for i in range(1, number + 1):
    if not number % i:
        print(i)

number = str(int(input("write the number: ")))
lst = []
for i, j in enumerate(number[::-1]):
    lst.append(f"({j}*10^{i})")
print(" + ".join(lst[::-1]))
