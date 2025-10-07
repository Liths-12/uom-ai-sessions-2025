# Project Euler Problem 10: Summation of primes
def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True 
def sum_of_primes_below(limit):
    return sum(i for i in range(2, limit) if is_prime(i))
print(sum_of_primes_below(2000000))
# Output: 142913828922  
# Time Complexity: O(n sqrt n)
# Space Complexity: O(1)
