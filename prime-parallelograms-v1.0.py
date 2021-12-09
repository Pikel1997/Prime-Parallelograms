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


# function which takes the prime number, converts it to base 2,
# reverses the digits and converts it back to decimal.
def function_on_primes():
    global list_of_ret_func
    list_of_ret_func = []
    for x in list_of_primes:
        gb = str(bin(x).replace("0b", ""))[::-1]
        list_of_ret_func.append(int(str(gb), 2))
    list_of_ret_func = list(map(int, list_of_ret_func))


# subtracting the function from the list of prime numbers.
def subtract_arrays():
    g = np.subtract(np.array(list_of_primes), np.array(list_of_ret_func))
    plt.scatter(np.array(list_of_primes), g, s=1)


n = int(input("enter number- "))
prime_numbers(n)
function_on_primes()
subtract_arrays()

# plotting
plt.title("Prime Parallelograms")
plt.xlabel("f(p(n)")
plt.ylabel("Prime Numbers")
plt.gca().spines['top'].set_visible(False)
plt.gca().spines['right'].set_visible(False)
plt.show()
