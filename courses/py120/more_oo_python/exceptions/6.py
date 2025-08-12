def invert_numbers(numbers):
    result = []
    for num in numbers:
        try:
            result.append(1/ num)
        except ZeroDivisionError:
            result.append(float('inf'))
    
    return result