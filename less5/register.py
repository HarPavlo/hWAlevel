def upp(lst):
    return lst.upper()


def low(lst):
    return lst.lower()


print("Uppercase: ", " ".join(list(map(upp, input("please write string: ").split()))))
print("Lower_case: ", " ".join(list(map(low, input("please write string: ").split()))))
