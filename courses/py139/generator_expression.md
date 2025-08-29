# Python Generators Study Guide

## Basic Questions

### 1. Basic: Create a generator expression that generates the reciprocals of the numbers from 1 to 10. A reciprocal of a number `n` is `1 / n`. Use a `for` loop to print each value.




**Answer:**
```python
# Generator expression for reciprocals
#reciprocals = (1 / n for n in range(1, 11))

def recip(max_range):

    for num in (1, max_range):
        yield 1 / n


# Print each value using a for loop
for value in recip:
    print(value)
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

### 2. Basic: Use a generator expression to capitalize every string in a list of strings. Use a single `print` invocation to print all the capitalized strings as a tuple.

**Answer:**
```python
strings = ['hello', 'world', 'python', 'programming']

# Generator expression to capitalize strings
capitalized = (string.capitalize() for string in strings)

# Print as tuple
print(tuple(capitalized))
# Output: ('Hello', 'World', 'Python', 'Programming')
```

### 3. Intermediate: Use a generator expression to capitalize the strings in a list of strings whose length is at least 5. Use a single `print` invocation to print all the capitalized strings as a set.

**Answer:**
```python
strings = ['cat', 'hello', 'world', 'python', 'programming', 'dog']

# Generator expression with condition (length >= 5)
long_capitalized = (string.capitalize() for string in strings if len(string) >= 5)

# Print as set
print(set(long_capitalized))
# Output: {'Hello', 'World', 'Python', 'Programming'}
# Note: Order may vary since sets are unordered
```

### 4. Basic: Create a generator function that generates the reciprocals of the numbers from 1 to n, where n is an argument to the function. Use a for loop to print each value for n=7.






**Answer:**
```python
def reciprocals(n):
    for number in range(1, n + 1):
        yield 1 / number

# Use the generator function
for value in reciprocals(7):
    print(value)
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
```

### 5. Basic: Create a generator function that generates the capitalized version of every string in a list of strings. Use a single print invocation to print all the capitalized strings as a tuple.
strings = ['four', 'score', 'and', 'seven', 'years', 'ago']



**Answer:**
```python
strings = ['four', 'score', 'and', 'seven', 'years', 'ago']

def capitalize(strings):
    for string in strings:
        yield string.capitalize()

print(tuple(capitalize(strings)))
# Output: ('Four', 'Score', 'And', 'Seven', 'Years', 'Ago')
```

capital_strings = (string.capitalize() for string in list_of_strings if len(string) < 5)
## Intermediate Questions

### 6. Intermediate: Create a generator function that generates the capitalized version of every string in a list of strings whose length is less than 5. Use a single print invocation to print all the capitalized strings as a set.

**Answer:**
```python
def capitalize_short(strings):
    for string in strings:
        if len(string) < 5:
            yield string.capitalize()

strings = ['four', 'score', 'and', 'seven', 'years', 'ago']
print(set(capitalize_short(strings)))
# Output: {'Four', 'And', 'Ago'}
# Note: The words may appear in a different order since sets are unordered
```

### 7. Intermediate: Consider the following nested dictionary. Use a generator expression and the sum() function to compute and display the total age of the family's male members. The result should be 444.

```python
munsters = {
    'Herman':  {'age': 32,  'gender': 'male'},
    'Lily':    {'age': 30,  'gender': 'female'},
    'Grandpa': {'age': 402, 'gender': 'male'},
    'Eddie':   {'age': 10,  'gender': 'male'},
    'Marilyn': {'age': 23,  'gender': 'female'},
}
```

**Answer:**
```python
munsters = {
    'Herman':  {'age': 32,  'gender': 'male'},
    'Lily':    {'age': 30,  'gender': 'female'},
    'Grandpa': {'age': 402, 'gender': 'male'},
    'Eddie':   {'age': 10,  'gender': 'male'},
    'Marilyn': {'age': 23,  'gender': 'female'},
}

# Generator expression to get ages of male members
male_ages = (member['age'] for member in munsters.values()
                           if member['gender'] == 'male')

total_male_age = sum(male_ages)
print(total_male_age)  # Output: 444
```

**Explanation:**
- Herman: 32 + Grandpa: 402 + Eddie: 10 = 444

### 8. Intermediate: Given the following data structure, use a generator expression to create a generator that yields each sublist ordered in ascending order. Convert the generator to a list and print the result.

```python
lst = [['b', 'c', 'a'], [2, 11, -3], ['blue', 'black', 'green']]
```

The expected result is `[['a', 'b', 'c'], [-3, 2, 11], ['black', 'blue', 'green']]`.

**Answer:**
```python
lst = [['b', 'c', 'a'], [2, 11, -3], ['blue', 'black', 'green']]

# Generator expression to sort each sublist
sorted_generator = (sorted(sublist) for sublist in lst)

# Convert to list and print
print(list(sorted_generator))
# Output: [['a', 'b', 'c'], [-3, 2, 11], ['black', 'blue', 'green']]
```

## Advanced Questions

### 9. Advanced: Given the following data structure, use a generator expression to create a generator that yields each sublist ordered in ascending order **as strings** (that is, the numbers should be treated as strings). Convert the generator to a list and print the result.

```python
lst = [['b', 'c', 'a'], [2, 11, -3], ['blue', 'black', 'green']]
```

The expected result is `[['a', 'b', 'c'], [-3, 11, 2], ['black', 'blue', 'green']]`.

**Answer:**
```python
lst = [['b', 'c', 'a'], [2, 11, -3], ['blue', 'black', 'green']]

# Generator expression sorting by string representation
sorted_generator = (sorted(sublist, key=str) for sublist in lst)

# Convert to list and print
print(list(sorted_generator))
# Output: [['a', 'b', 'c'], [-3, 11, 2], ['black', 'blue', 'green']]
```

**Explanation:**
- When sorting numbers as strings: `-3` < `11` < `2` (lexicographic order)
- This is because string comparison is character by character: `-` < `1` < `2`

## Additional Generator Concepts and Examples

### Generator Expressions vs List Comprehensions

**List Comprehension (creates entire list in memory):**
```python
# Creates a list immediately
squares_list = [x**2 for x in range(10)]
print(type(squares_list))  # <class 'list'>
```

**Generator Expression (lazy evaluation):**
```python
# Creates a generator object
squares_gen = (x**2 for x in range(10))
print(type(squares_gen))  # <class 'generator'>

# Values are generated on-demand
for square in squares_gen:
    print(square)
```

### Generator Functions vs Generator Expressions

**Generator Function:**
```python
def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b

# Usage
fib_gen = fibonacci(10)
print(list(fib_gen))  # [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
```

**Generator Expression (for simple cases):**
```python
# Simple generator expression
even_squares = (x**2 for x in range(20) if x % 2 == 0)
print(list(even_squares))  # [0, 4, 16, 36, 64, 100, 144, 196, 256, 324]
```

### Memory Efficiency Example

```python
# Memory-efficient processing of large datasets
def process_large_file():
    # Generator that processes one line at a time
    def read_lines():
        # Simulating file reading
        for i in range(1000000):
            yield f"Line {i}: Some data"
    
    # Process without loading everything into memory
    processed = (line.upper() for line in read_lines() if 'data' in line)
    
    # Only process what we need
    for i, line in enumerate(processed):
        if i >= 5:  # Only process first 5 matching lines
            break
        print(line)

# This uses minimal memory regardless of file size
```

### Chaining Generators

```python
def numbers(start, end):
    for i in range(start, end):
        yield i

def squares(nums):
    for num in nums:
        yield num ** 2

def filter_even(nums):
    for num in nums:
        if num % 2 == 0:
            yield num

# Chain generators together
result = filter_even(squares(numbers(1, 11)))
print(list(result))  # [4, 16, 36, 64, 100]
```

## Key Takeaways

### Generator Expressions
- **Syntax**: `(expression for item in iterable if condition)`
- **Memory efficient**: Values generated on-demand
- **Single-use**: Can only be iterated once
- **Lazy evaluation**: Values computed when requested

### Generator Functions
- **Use `yield` keyword** instead of `return`
- **State is preserved** between yields
- **More flexible** than generator expressions
- **Can have complex logic** and multiple yield points

### When to Use Generators
1. **Large datasets** that don't fit in memory
2. **Infinite sequences** (like Fibonacci)
3. **Pipeline processing** with chained operations
4. **Memory-critical applications**
5. **When you don't need all values at once**

### Common Built-in Functions with Generators
- `sum()` - works with any iterable, including generators
- `max()`, `min()` - can consume generators
- `any()`, `all()` - short-circuit evaluation with generators
- `enumerate()`, `zip()` - return iterators that work like generators