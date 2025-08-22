#assert condition, message

def add(a, b):
    return a + b

assert(add(4,4) == 7), "Add function failed"

is_active = True
assert is_active, "boolean check"

assert get_max(10,20) > 15, "check to see if it returns greater then number"

assert 2 in numbers, "check if number in list"

try:
    x = 1/0
    assert False, "Exception check failed, no exception raised"
except ZeroDivisionError:
    pass
