# 6 kyu

# Define a function isPrime/isPrime() that takes one integer argument
# returns true/True or false/False depending on if the integer is a prime.
# Per Wikipedia, a prime number (or a prime) is a natural number greater
# than 1 that has no positive divisors other than 1 and itself.
# You can assume you will be given an integer input.
# You can not assume that the integer will be only positive.
# You may be given negative numbers as well (or 0).


def isPrime(number):
    if number <= 1:
        print("False")
        return False  # early exit
    for i in range(2, number - 1):
        if number % i == 0:
            print("False")
            return False
    print("True")
    return True


if __name__ == "__main__":
    isPrime(0)  # False
    isPrime(1)  # False
    isPrime(2)  # True
    isPrime(3)  # True
    isPrime(4)  # False
    isPrime(5)  # True
    isPrime(6)  # False
    isPrime(7)  # True
    isPrime(8)  # False
    isPrime(9)  # False
