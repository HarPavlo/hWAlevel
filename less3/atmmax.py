amount = int(input("enter amount: "))
L = [1000, 500, 200, 100, 50, 20, 10, 5, 2, 1]
lst = []
for den in L:
    if amount / den >= 1:
        quan = amount // den
        amount -= quan * den
        lst.append(f"({quan} * {den})")
print(" + ".join(lst))
