
'''
we need to find every permutation of a substring and return a list.
to find every permutation of a substring we can loop the string
    have an inside loop tht goes from the index of the first loop increment
    by 1 until end of string
    append each one of these substrings to a list

have a different function that goes through the permutation list
converts it to a number
decides if it is even
return a counter for each even number
'''
def even_substrings(string):
    our_numbers = permutations(string)
    total = 0
    for num in our_numbers:
        if int(num) % 2 == 0:
            total += 1

    return total

def permutations(string):
    return_list = []
    counter = 0

    while counter < len(string):
        placeholder = 1
        
        while placeholder < len(string) + 1:
            substring = string[counter:placeholder]
            if len(substring) >= 1:
                return_list.append(substring)
            placeholder += 1
        
        counter += 1



    return return_list

print(permutations('1432'))


print(even_substrings('1432') == 6)
print(even_substrings('3145926') == 16)
print(even_substrings('2718281') == 16)
print(even_substrings('13579') == 0)
print(even_substrings('143232') == 12)