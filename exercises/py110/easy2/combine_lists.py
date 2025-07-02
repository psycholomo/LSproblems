
def union(arr1, arr2):
    myset = set()

    for num in arr1:
        if num not in myset:
            myset.add(num)
    for num in arr2:
        if num not in myset:
            myset.add(num)
    return myset

print(union([1, 3, 5], [3, 6, 9]) == {1, 3, 5, 6, 9}) # True