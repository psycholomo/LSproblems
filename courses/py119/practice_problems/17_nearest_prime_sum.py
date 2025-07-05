'''
sum up the total of the numbers
increase by 1 and check to see if it is prime
if it is prime, return the count to the prime

create a function to find prime
'''
import math
def nearest_prime_sum(arr):

    sum = 0

    for i in arr:
        sum += i

    count = 0

    for num in range(sum + 1, 1000):
        count += 1
        if find_prime(num):
            break
        
    return count


def find_prime(num):

    if num < 2:
        return False
    
    if num == 2:
        return True
    
    if num % 2 == 0:
        return False
    
    for i in range(3, num):
        if num % i == 0:
            return False
    

    return True
    '''
    to find a prime,
    check to see if the number is less then 2
    check to see if the number is equal to 2.
        if 2 return true
    check to see if the number is even
    if it is even, it is not prime

    check the number in range. by going from 2 to the square root of the number up to the number we are looking for
    if the number %2 == 0 then return False
    otherwise return True
    need to import math for .sqrt function

    '''


print(nearest_prime_sum([1, 2, 3]) == 1)        # Nearest prime to 6 is 7
print(nearest_prime_sum([5, 2]) == 4)           # Nearest prime to 7 is 11
print(nearest_prime_sum([1, 1, 1]) == 2)        # Nearest prime to 3 is 5
print(nearest_prime_sum([2, 12, 8, 4, 6]) == 5) # Nearest prime to 32 is 37

# Nearest prime to 163 is 167
print(nearest_prime_sum([50, 39, 49, 6, 17, 2]) == 4)