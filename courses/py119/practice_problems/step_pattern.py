
'''
input is an integer,
output is a list of stars and spaces based on that integer
if it is 3, we will have 3 outputs.

the way to solve this is to keep track of spaces and stars
if the length is 1, just return a star
if the length is less then 1 return an empty list
to start the number of spaces is the number -1
the stars is the number of spaces minus the num

we then looop through and decrement the number of spaces while
increasing the of stars until we hit our number

'''

def step_pattern(num):
    my_list = []
    if num == 1:
        return ["*"]
    if num <= 1:
        return my_list
    
    spaces = num - 1
    stars = num - spaces 

    for i in range(num):
        my_list.append(f'{" " *spaces}{"*" * stars}')
        spaces -= 1
        stars += 1
    
    return my_list

print(step_pattern(3))
# step_pattern(3)
# Output:
# ['  *',
#  ' **',
#  '***']
