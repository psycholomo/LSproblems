'''
input is an array
return is a tuple with two numbers
we want to find the two numbers that are closest in value
to find closest in value we can subtract two numbers, and if the number is lowest,
we found our numbers
all numbers are unique
loop through array
    loop through the array again
        if the number is the same, continue
    take the absolute value if current number - initial number
    if the difference is smaller then smallest number,
    push tuplet,
    update the min number

    return the tuple



'''

def closest_numbers(arr):


print(closest_numbers([5, 25, 15, 11, 20]) == (15, 11))
print(closest_numbers([19, 25, 32, 4, 27, 16]) == (25, 27))
print(closest_numbers([12, 22, 7, 17]) == (12, 7))