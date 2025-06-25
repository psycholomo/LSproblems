def multisum(num):
    returnSum = 0
    seenNums = []
    for i in range (3, num + 1, 3):
        seenNums.append(i)
        returnSum += i
    
    for i in range (5, num + 1, 5):
        if i not in seenNums:
            returnSum += i
     
    
    return returnSum


print(multisum(3) == 3)
print(multisum(5) == 8)
print(multisum(10) == 33)
print(multisum(1000) == 234168)