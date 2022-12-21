import math
def largest_prime_factor(n):
    for i in range(2, math.floor(math.sqrt(n)) + 1, 1):
        if (n % i == 0):
            return largest_prime_factor(n//i)
    return n
a = 600851475143
print("the largest prime factor of the number {} is {}".format(a, largest_prime_factor(a)))