# Python Generator Expressions and Functions - Practice Exercises with Solutions

## 1. **Basic**: Generator Expression for Reciprocals (1-10)
Create a generator expression that generates the reciprocals of the numbers from 1 to 10. A reciprocal of a number `n` is `1 / n`. Use a `for` loop to print each value.

**Solution:**
```python
reciprocals = (1 / n for n in range(1, 11))
for reciprocal in reciprocals:
    print(reciprocal)
```

**Output:**
```
1.0
0.5
0.3333333333333333
0.25
0.2
0.16666666666666666
0.14285714285714285
0.125
0.1111111111111111
0.1
```

## 2. **Basic**: Generator Function for Reciprocals (1 to n)
Create a generator function that generates the reciprocals of the numbers from 1 to `n`, where `n` is an argument to the function. Use a `for` loop to print each value.

**Solution:**
```python
def reciprocals_generator(n):
    for i in range(1, n + 1):
        yield 1 / i

# Example usage:
for reciprocal in reciprocals_generator(5):
    print(reciprocal)
```

**Output:**
```
1.0
0.5
0.3333333333333333
0.25
0.2
```

## 3. **Intermediate**: Generator Expression to Capitalize Strings
Use a generator expression to capitalize every string in a list of strings. Use a single `print` invocation to print all the capitalized strings as a tuple.

**Solution:**
```python
strings = ['hello', 'world', 'python', 'programming']
capitalized = (s.capitalize() for s in strings)
print(tuple(capitalized))
```

**Output:**
```
('Hello', 'World', 'Python', 'Programming')
```

## 4. **Intermediate**: Generator Function to Capitalize Strings
Create a generator function that generates the capitalized version of every string in a list of strings. Use a single `print` invocation to print all the capitalized strings as a tuple.

**Solution:**
```python
def capitalize_strings(string_list):
    for s in string_list:
        yield s.capitalize()

# Example usage:
strings = ['hello', 'world', 'python', 'programming']
print(tuple(capitalize_strings(strings)))
```

**Output:**
```
('Hello', 'World', 'Python', 'Programming')
```

## 5. **Intermediate**: Generator Expression with Length Filter (≥5)
Use a generator expression to capitalize the strings in a list of strings whose length is at least 5. Use a single `print` invocation to print all the capitalized strings as a set.

**Solution:**
```python
strings = ['hi', 'hello', 'world', 'python', 'programming', 'code']
capitalized_long = (s.capitalize() for s in strings if len(s) >= 5)
print(set(capitalized_long))
```

**Output:**
```
{'Hello', 'World', 'Python', 'Programming'}
```

## 6. **Intermediate**: Generator Function with Length Filter (<5)
Create a generator function that generates the capitalized version of every string in a list of strings whose length is less than 5. Use a single `print` invocation to print all the capitalized strings as a set.

**Solution:**
```python
def capitalize_short_strings(string_list):
    for s in string_list:
        if len(s) < 5:
            yield s.capitalize()

# Example usage:
strings = ['hi', 'hello', 'world', 'python', 'programming', 'code']
print(set(capitalize_short_strings(strings)))
```

**Output:**
```
{'Hi', 'Code'}
```

## 7. **Intermediate**: Unscramble Function
Create a function that takes two strings as arguments and returns `True` if some portion of the characters in the first string can be rearranged to match the characters in the second. Otherwise, the function should return `False`.

You may assume that both string arguments only contain lowercase alphabetic characters. Neither string will be empty.

**Solution:**
```python
def unscramble(scrambled, target):
    # Count characters in both strings
    scrambled_count = {}
    target_count = {}
    
    for char in scrambled:
        scrambled_count[char] = scrambled_count.get(char, 0) + 1
    
    for char in target:
        target_count[char] = target_count.get(char, 0) + 1
    
    # Check if scrambled has enough of each character needed for target
    for char, needed in target_count.items():
        if scrambled_count.get(char, 0) < needed:
            return False
    
    return True

# Test cases:
print(unscramble('ansucchlohlo', 'launchschool') == True)
print(unscramble('phyarunstole', 'pythonrules') == True)
print(unscramble('phyarunstola', 'pythonrules') == False)
print(unscramble('boldface', 'coal') == True)
print(unscramble('olc', 'cool') == False)
```

**Alternative solution using Counter:**
```python
from collections import Counter

def unscramble(scrambled, target):
    scrambled_count = Counter(scrambled)
    target_count = Counter(target)
    
    for char, needed in target_count.items():
        if scrambled_count[char] < needed:
            return False
    
    return True
```

## 8. **Intermediate**: Seven Eleven Sum
Create a function that takes a single integer argument and returns the sum of all the multiples of 7 or 11 that are less than the argument. If a number is a multiple of both 7 and 11, count it just once.

For example, the multiples of 7 and 11 that are below 25 are 7, 11, 14, 21, and 22. The sum of these multiples is 75.

If the argument is negative, return 0.

**Solution:**
```python
def seven_eleven(n):
    if n <= 0:
        return 0
    
    total = 0
    for i in range(1, n):
        if i % 7 == 0 or i % 11 == 0:
            total += i
    
    return total

# Test cases:
print(seven_eleven(10) == 7)
print(seven_eleven(11) == 7)
print(seven_eleven(12) == 18)
print(seven_eleven(25) == 75)
print(seven_eleven(100) == 1153)
print(seven_eleven(0) == 0)
print(seven_eleven(-100) == 0)
```

**Alternative solution using generator expression:**
```python
def seven_eleven(n):
    if n <= 0:
        return 0
    
    return sum(i for i in range(1, n) if i % 7 == 0 or i % 11 == 0)
```

## 9. **Advanced**: Greatest Product of Four Consecutive Digits
Create a function that takes a string argument that consists entirely of numeric digits and computes the greatest product of four consecutive digits in the string.

The argument will always have more than 4 digits.

**Solution:**
```python
def greatest_product(digits_str):
    max_product = 0
    
    for i in range(len(digits_str) - 3):
        # Get four consecutive digits
        four_digits = digits_str[i:i+4]
        
        # Calculate product of these four digits
        product = 1
        for digit in four_digits:
            product *= int(digit)
        
        # Update maximum if this product is greater
        max_product = max(max_product, product)
    
    return max_product

# Test cases:
print(greatest_product('23456') == 360)      # 3 * 4 * 5 * 6
print(greatest_product('3145926') == 540)    # 5 * 9 * 2 * 6
print(greatest_product('1828172') == 128)    # 1 * 8 * 2 * 8
print(greatest_product('123987654') == 3024) # 9 * 8 * 7 * 6
```

**Alternative solution using reduce:**
```python
from functools import reduce
import operator

def greatest_product(digits_str):
    max_product = 0
    
    for i in range(len(digits_str) - 3):
        four_digits = [int(d) for d in digits_str[i:i+4]]
        product = reduce(operator.mul, four_digits)
        max_product = max(max_product, product)
    
    return max_product
```

## 10. **Advanced**: Distinct Multiples Count
Create a function that returns the count of distinct case-insensitive alphabetic characters and numeric digits that occur more than once in the input string. You may assume that the input string contains only alphanumeric characters.

**Solution:**
```python
def distinct_multiples(s):
    # Convert to lowercase for case-insensitive comparison
    s = s.lower()
    
    # Count occurrences of each character
    char_count = {}
    for char in s:
        char_count[char] = char_count.get(char, 0) + 1
    
    # Count characters that appear more than once
    multiple_count = 0
    for count in char_count.values():
        if count > 1:
            multiple_count += 1
    
    return multiple_count

# Test cases:
print(distinct_multiples('xyz') == 0)               # (none)
print(distinct_multiples('xxyypzzr') == 3)          # x, y, z
print(distinct_multiples('xXyYpzZr') == 3)          # x, y, z
print(distinct_multiples('unununium') == 2)         # u, n
print(distinct_multiples('multiplicity') == 3)      # l, t, i
print(distinct_multiples('7657') == 1)              # 7
print(distinct_multiples('3141592653589793') == 4)  # 3, 1, 5, 9
print(distinct_multiples('2718281828459045') == 5)  # 2, 1, 8, 4, 5
```

**Alternative solution using Counter:**
```python
from collections import Counter

def distinct_multiples(s):
    char_count = Counter(s.lower())
    return sum(1 for count in char_count.values() if count > 1)
```

**Alternative solution using generator expression:**
```python
def distinct_multiples(s):
    s = s.lower()
    char_count = {}
    for char in s:
        char_count[char] = char_count.get(char, 0) + 1
    
    return sum(1 for count in char_count.values() if count > 1)
```