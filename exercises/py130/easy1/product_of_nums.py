from functools import reduce
nums =[1,2,3,4,5]

def product(x,y):
    return x * y
calculated = reduce(product, nums)
print(calculated)