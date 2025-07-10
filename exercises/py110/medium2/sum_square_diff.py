'''
we need to square each number and then sum the numbers
together
have a sum number and set it to 0

if number is 1 or less return 0
otherwise
for each number in range from 1 to the number
square the numbmer
add it to our sum
return the sum
'''

def sum_square_difference(num):
    sum = 0
    difference = 0

    if num <= 1:
        return sum
    for i in range(1, num + 1):
        
        sum = sum + (i ** 2)
        difference += i
    
    
    return (difference) ** 2 - sum

print(sum_square_difference(3) == 22)          # True
# 22 --> (1 + 2 + 3)**2 - (1**2 + 2**2 + 3**2)

print(sum_square_difference(10) == 2640)       # True
print(sum_square_difference(1) == 0)           # True
print(sum_square_difference(100) == 25164150)  # True