numbers = [1,2,3,4,5]

def try_this(num):
    if num %2 == 0:
        return num

selected = filter(lambda x: x % 2 == 0, numbers)
print(list(selected))