#problem 1 : Multiples of 3 and 5
def sum_of_multiples(limit):
    return sum(x for x in range(limit) if x % 3 == 0 or x % 5 == 0) 
print(sum_of_multiples(1000))       
#Output: 233168
#Time Complexity: O(n)
#Space Complexity: O(1)





