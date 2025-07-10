'''
the featured number rules are that it has to be odd, it has to be divisble by 7
and their cant be any repeating numbers in the number

create a helper function that converts the number to a string
creates a dictionary of counts
if any count is greater then 2 > return False
otherwise return True

main function 
use a while loop to count from the number + 1
if the number is divisble by 7 i.e number % 7 == 0
check to see if its odd
check to see if count is higher then 2
if both return True
return the number
break the while loop
'''


def next_featured(num):
    counter = num + 1
    while True:

        if check_valid(counter):
            break
        counter += 1
    
    return counter



def check_valid(num):

    count_nums = {}

    if num % 2 == 1 and num % 7 == 0:
        num_string = str(num)
        for value in num_string:
            if value in count_nums:
                count_nums[value] += 1
            else:
                count_nums[value] = 1
        for value in count_nums.values():
            if value >= 2:
                return False
        return True
    return False



print(next_featured(12) == 21)                  # True
print(next_featured(20) == 21)                  # True
print(next_featured(21) == 35)                  # True
print(next_featured(997) == 1029)               # True
print(next_featured(1029) == 1043)              # True
print(next_featured(999999) == 1023547)         # True
print(next_featured(999999987) == 1023456987)   # True
print(next_featured(9876543186) == 9876543201)  # True
print(next_featured(9876543200) == 9876543201)  # True

error = ("There is no possible number that "
         "fulfills those requirements.")
print(next_featured(9876543201) == error)       # True