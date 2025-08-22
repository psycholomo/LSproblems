lists = [1,2,3,[4,5,6],7]

first_list = (value for sublist in lists for value in sublist)

for value in first_list:
    print(value)