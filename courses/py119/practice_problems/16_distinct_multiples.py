
'''
create an empty dictionary
loop through the characters
collect a count
if the count of the character is 2 or greater,
push the letter to a set
return the set
if the list is empty,
return None

'''


def distinct_multiples(string):
    my_dict = {}
    my_set = set()

    for char in string:
        lower_char = char.lower()

        if lower_char in my_dict:
            my_dict[lower_char] += 1
        else:
            my_dict[lower_char] = 1
        
        if my_dict[lower_char] >= 2:
            my_set.add(lower_char)
    
    return len(my_set)
    


print(distinct_multiples('xyz') == 0)               # (none)
print(distinct_multiples('xxyypzzr') == 3)          # x, y, z
print(distinct_multiples('xXyYpzZr') == 3)          # x, y, z
print(distinct_multiples('unununium') == 2)         # u, n
print(distinct_multiples('multiplicity') == 3)      # l, t, i
print(distinct_multiples('7657') == 1)              # 7
print(distinct_multiples('3141592653589793') == 4)  # 3, 1, 5, 9
print(distinct_multiples('2718281828459045') == 5)  # 2, 1, 8, 4, 5