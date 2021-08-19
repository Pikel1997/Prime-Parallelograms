import numpy as np
import matplotlib.pyplot as plt

np.set_printoptions(threshold=1000000)


# function to get all the prime numbers from 1 to n.
def prime_numbers(n):
    global list_of_primes
    list_of_primes = []
    for num in range(2, n+1):
        if all(num % i != 0 for i in range(2, num)):
            list_of_primes.append(num)
    # print(np.array(list_of_primes))


# function to convert the prime numbers to base 2.
def bin_of_primes():
    global list_of_binary
    list_of_binary = []
    for x in list_of_primes:
        list_of_binary.append(bin(x).replace("0b", ""))
    list_of_binary = list(map(int, list_of_binary))
    # print(np.array(list_of_binary))


# function to reverse the digits of the base 2 number.
def rev_bin_of_primes():
    global list_of_rev_binary
    list_of_rev_binary = []
    for y in list_of_binary:
        list_of_rev_binary.append(str(y)[::-1])
    list_of_rev_binary = list(map(int, list_of_rev_binary))
    # print(np.array(list_of_rev_binary))


# function to convert the binary number to decimal.
def dec_of_rev_bin_of_primes():
    global list_of_dec_of_rev_binary
    list_of_dec_of_rev_binary = []
    for z in list_of_rev_binary:
        list_of_dec_of_rev_binary.append(int(str(z), 2))
    # print(np.array(list_of_dec_of_rev_binary))


# subtracting the function from the list of prime numbers.
def subtract_arrays():
    g = np.subtract(np.array(list_of_primes), np.array(list_of_dec_of_rev_binary))
    # print(g)
    plt.scatter(np.array(list_of_primes), g, s=1)


n = int(input("enter number- "))
prime_numbers(n)
bin_of_primes()
rev_bin_of_primes()
dec_of_rev_bin_of_primes()
subtract_arrays()

# plotting
plt.title("Prime Parallelograms")
plt.xlabel("f(p(n)")
plt.ylabel("Prime Numbers")
plt.gca().spines['top'].set_visible(False)
plt.gca().spines['right'].set_visible(False)
plt.show()
