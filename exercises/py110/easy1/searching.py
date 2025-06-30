#Write a program that solicits six (6) numbers from the user and prints a message that describes whether the sixth number appears among the first five.
#create an array with all set numbers
# set a variable with the last number in the array
# creat a set from the array
# if the number is in the set
# print out message with all the numbers in set
# otherwise print all numbers in set

myArr = [25,15,20,17,23,17]
lastDigit = myArr.pop()
mySet = set(myArr)
buildStr = []
for digits in myArr:
    buildStr.append(str(digits))
buildStr = ",".join(buildStr)
if lastDigit in mySet:
    print(f"{lastDigit} is in {buildStr}")
else:
    print(f"{lastDigit} is not in {buildStr}")

