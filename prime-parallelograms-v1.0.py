import numpy as np
import matplotlib.pyplot as plt

np.set_printoptions(threshold=1000000)


# function to get all the prime numbers from 1 to n.


def SieveOfAtkin(n):
    global list_of_primes
    list_of_primes = []
    # 2 and 3 are known
    # to be prime
    if n > 2:
        list_of_primes.append(2)
    if n > 3:
        list_of_primes.append(3)

    # Initialise the sieve
    # array with False values
    sieve = [False] * n
    for i in range(0, n):
        sieve[i] = False

    '''Mark sieve[n] is True if
    one of the following is True:
    a) n = (4*x*x)+(y*y) has odd
    number of solutions, i.e.,
    there exist odd number of
    distinct pairs (x, y) that
    satisfy the equation and
    n % 12 = 1 or n % 12 = 5.
    b) n = (3*x*x)+(y*y) has
    odd number of solutions
    and n % 12 = 7
    c) n = (3*x*x)-(y*y) has
    odd number of solutions,
    x > y and n % 12 = 11 '''
    x = 1
    while x * x < n:
        y = 1
        while y * y < n:

            # Main part of
            # Sieve of Atkin
            nq = (4 * x * x) + (y * y)
            if (nq <= n and (nq % 12 == 1 or
                                nq % 12 == 5)):
                sieve[nq] ^= True

            nq = (3 * x * x) + (y * y)
            if nq <= n and nq % 12 == 7:
                sieve[nq] ^= True

            nq = (3 * x * x) - (y * y)
            try:
                if (x > y and n <= n and
                        nq % 12 == 11):
                    sieve[nq] ^= True
            except IndexError:
                pass
            y += 1
        x += 1

    # Mark all multiples of
    # squares as non-prime
    r = 5
    while r * r < n:
        if sieve[r]:
            for i in range(r * r, n, r * r):
                sieve[i] = False

        r += 1

        # Print primes
    # using sieve[]
    for a in range(5, n):
        if sieve[a]:
            list_of_primes.append(a)


# function which takes the prime number, converts it to base 2,
# reverses the digits and converts it back to decimal.
def function_on_primes():
    global list_of_ret_func
    list_of_ret_func = []
    for xa in list_of_primes:
        gb = str(bin(xa).replace("0b", ""))[::-1]
        list_of_ret_func.append(int(str(gb), 2))
    list_of_ret_func = list(map(int, list_of_ret_func))


# subtracting the function from the list of prime numbers.
def subtract_arrays():
    g = np.subtract(np.array(list_of_primes), np.array(list_of_ret_func))
    plt.scatter(np.array(list_of_primes), g, s=1)


n = int(input("enter number- "))
SieveOfAtkin(n)
function_on_primes()
subtract_arrays()

# plotting
plt.title("Prime Parallelograms")
plt.xlabel("f(p(n)")
plt.ylabel("Prime Numbers")
plt.gca().spines['top'].set_visible(False)
plt.gca().spines['right'].set_visible(False)
plt.show()
