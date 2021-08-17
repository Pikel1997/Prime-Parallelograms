import numpy as np
import matplotlib.pyplot as plt

np.set_printoptions(threshold=1000000)


def prime_numbers(n):
    global list_of_primes
    list_of_primes = []
    for num in range(2, n+1):
        if all(num % i != 0 for i in range(2, num)):
            list_of_primes.append(num)
    # print(np.array(list_of_primes))


def bin_of_primes():
    global list_of_binary
    list_of_binary = []
    for x in list_of_primes:
        list_of_binary.append(bin(x).replace("0b", ""))
    list_of_binary = list(map(int, list_of_binary))
    # print(np.array(list_of_binary))


def rev_bin_of_primes():
    global list_of_rev_binary
    list_of_rev_binary = []
    for y in list_of_binary:
        list_of_rev_binary.append(str(y)[::-1])
    list_of_rev_binary = list(map(int, list_of_rev_binary))
    # print(np.array(list_of_rev_binary))


def dec_of_rev_bin_of_primes():
    global list_of_dec_of_rev_binary
    list_of_dec_of_rev_binary = []
    for y in list_of_rev_binary:
        list_of_dec_of_rev_binary.append(int(str(y), 2))
    # print(np.array(list_of_dec_of_rev_binary))


def subtract_arrays():
    print(np.subtract(np.array(list_of_primes), np.array(list_of_dec_of_rev_binary)))


n = int(input("enter number- "))
prime_numbers(n)
bin_of_primes()
rev_bin_of_primes()
dec_of_rev_bin_of_primes()
subtract_arrays()

# plotting
plt.title("Prime Parallelograms")
plt.xlabel("Iterations/Steps")
plt.ylabel("Numbers")
plt.gca().spines['top'].set_visible(False)
plt.gca().spines['right'].set_visible(False)
plt.grid()
plt.show()
