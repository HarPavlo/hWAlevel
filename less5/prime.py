# Square a prime number
def prime(number):
    for i in range(2, number):
        if number % i == 0:
            print("Nonprime number. Try again!")
            exit()
    else:
        return number**2

print(prime(int(input("enter number: "))))


# Square a prime number in the list
def prime(number):
    for i in range(2, number):
        if number % i == 0:
            number = number
            break
    else:
        number = number**2
    return number

print(list(map(prime, list(range(2, int(input("enter the last number of the list: "))+1)))))