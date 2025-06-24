#1
numbers = [1, 2, 3, 4, 5]   
#can reverse doing a for loop and putting all elements in a new list
new_nums = numbers[::-1]
second_way = list(reversed(numbers))

#2 
numbers = [1, 2, 3, 4, 5, 15, 16, 17, 95, 96, 99]

number1 = 8  # False (not in numbers)
number2 = 95 # True (in numbers)

number1 in numbers
number2 in numbers

#3

42 in range(10, 101)          # True
100 in range(10, 101)         # True
101 in range(10, 101)         # False

#4
myList = [1,2,3,4,5]
myList.pop(2)
del myList[2]

#5
print(isinstance(myList, dict))
#6
mytitle = " " * 40
mytitle.center(40)

statement1 = "The Flinestones Rock!"
statement2 = "Easy come, easy go."

#7
statement1.count('t')

# 8
ages = {'Herman': 32, 'Lily': 30, 'Grandpa': 402, 'Eddie': 10}

my_var = "Herman" in ages
print(my_var)

#9
ages = {'Herman': 32, 'Lily': 30, 'Grandpa': 5843, 'Eddie': 10}
additional_ages = {'Marilyn': 22, 'Spot': 237}

for indx, (key, value) in enumerate(additional_ages.items()):
    ages[key] = value
    print(key)
print(ages)

ages.updates(additional_ages)