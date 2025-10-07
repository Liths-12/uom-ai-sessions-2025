#problem 3 : Largest prime factor
def largest_prime_factor(n):
    i = 2
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
    return n    
print(largest_prime_factor(600851475143))
#Output: 6857
#Time Complexity: O(sqrt(n))
#Space Complexity: O(1)
# The function iteratively divides n by its smallest prime factor until n becomes a prime number itself.
# The largest prime factor is then returned.
# This approach is efficient for large numbers due to its O(sqrt(n)) time complexity.
