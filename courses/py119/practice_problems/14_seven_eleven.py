

def seven_eleven(num):
    if num < 0:
        return 0
    count = []
    for i in range(num):

        if i % 7 == 0 or i % 11 == 0:
            count.append(i)

    sum = 0

    for i in count:
        sum += i
    return sum
    

print(seven_eleven(10) == 7)
print(seven_eleven(11) == 7)
print(seven_eleven(12) == 18)
print(seven_eleven(25) == 75)
print(seven_eleven(100) == 1153)
print(seven_eleven(0) == 0)
print(seven_eleven(-100) == 0)