'''
we need to get a substring of length of 5
generate the product from all the seperate digits
check to see if it is larger then a max number

the best way to do this is by looping through each
character in the string
grab the slice between i and i + 4
take that slice and turn it into a list
loop through the list of numbers
multiply them together
if they are greater then current max
update max
'''

def digit_product(my_str):

    maximum = 0
    for i in range(len(my_str)):
        my_slice = my_str[i:i+4]
        product = 1
        for char in my_slice:
            num = int(char)
            product *= num
        
        maximum = max(maximum, product)

    return maximum
            



input = '73167176531330624919225119674426574742355349194934'
# output: '94735'  # or similar (not the correct one above!)
print(digit_product(input))