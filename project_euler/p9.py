# Project Euler Problem 9: Special Pythagorean triplet
def find_special_pythagorean_triplet(sum_total):
    for a in range(1, sum_total):
        for b in range(a, sum_total - a):
            c = sum_total - a - b
            if a**2 + b**2 == c**2:
                return a * b * c
    return None 
print(find_special_pythagorean_triplet(1000))
# Output: 31875000  
# Time Complexity: O(n^2)
# Space Complexity: O(1)
