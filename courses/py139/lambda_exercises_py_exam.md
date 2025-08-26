# Python Lambda Functions - Practice Exercises with Answer Key

## Part 1: Conceptual Questions

### 1. **Difficulty: Basic**
What is the general syntax of a lambda function in Python?

**Answer:**
```python
lambda parameters: expression
```
The general syntax is `lambda` followed by zero or more parameters, a colon, and then a single expression that gets returned.

### 2. **Difficulty: Basic**
According to the course material, what are the main restrictions of lambda functions in Python? List at least three.

**Answer:**
- Lambda functions can only contain a single expression (no statements)
- They cannot contain assignments or variable declarations
- They cannot include control flow statements like `if`, `while`, or `for` (except in conditional expressions)
- They cannot contain `return`, `pass`, `assert`, or `raise` statements
- They are limited to simple expressions only

### 3. **Difficulty: Basic**
Why can lambda functions be difficult to debug compared to standard named functions?

**Answer:**
Lambda functions are anonymous and don't have descriptive names, making them harder to identify in stack traces and error messages. They also can't contain print statements or breakpoints for debugging purposes, and their single-expression limitation makes complex logic harder to troubleshoot.

### 4. **Difficulty: Basic**
In your own words, explain the primary difference between a lambda expression and a standard function defined with def.

**Answer:**
The primary difference is that lambda functions are anonymous, single-expression functions that return a value immediately, while `def` functions are named, can contain multiple statements and complex logic, and explicitly use `return` statements. Lambda functions are designed for simple, inline operations, while `def` functions are better for more complex, reusable code.

## Part 2: Syntax and Conversion

### 5. **Difficulty: Basic**
Convert the following function into a lambda expression and assign it to a variable named `add_bang`.

```python
def append_exclamation(text):
    return text + '!'
```

**Answer:**
```python
add_bang = lambda text: text + '!'
```

### 6. **Difficulty: Basic**
Convert the following lambda expression into a standard function definition using `def`.

```python
is_long_word = lambda word, length=8: len(word) > length
```

**Answer:**
```python
def is_long_word(word, length=8):
    return len(word) > length
```

### 7. **Difficulty: Intermediate**
What will the following code output?

```python
functions = [lambda i: i + 10, lambda i: i * 2, lambda i: i - 5]
result = 5
for func in functions:
    result = func(result)

print(result)
```

**Answer:**
```
25
```

**Explanation:**
- Start with `result = 5`
- First function: `5 + 10 = 15`
- Second function: `15 * 2 = 30`
- Third function: `30 - 5 = 25`

### 8. **Difficulty: Intermediate**
Identify the syntax error in the following lambda expression and explain why it is an error based on the rules for lambdas.

```python
# Goal: return the number if it's even, otherwise return None
process_number = lambda x: if x % 2 == 0: x
```

**Answer:**
The syntax error is that this uses an incomplete `if` statement. Lambda functions cannot contain statements like `if`, only expressions. The correct way would be to use a conditional expression (ternary operator):

```python
process_number = lambda x: x if x % 2 == 0 else None
```

## Part 3: Coding with Higher-Order Functions

### Using map

### 9. **Difficulty: Intermediate**
Given the list `numbers = [1, 2, 3, 4, 5]`, use `map` and a lambda function to create a new list containing the square of each number.

**Answer:**
```python
numbers = [1, 2, 3, 4, 5]
squares = list(map(lambda x: x**2, numbers))
# Result: [1, 4, 9, 16, 25]
```

### 10. **Difficulty: Intermediate**
Given the list `strings = ['hello', 'world', 'python']`, use `map` and a lambda function to create a new list where each string is capitalized.

**Answer:**
```python
strings = ['hello', 'world', 'python']
capitalized = list(map(lambda s: s.capitalize(), strings))
# Result: ['Hello', 'World', 'Python']
```

### 11. **Difficulty: Intermediate**
Given a list of names `names = ["  ada  ", "  grace ", " betty "]`, use `map` and a lambda function to create a new list where each name is properly capitalized and has leading/trailing whitespace removed.

**Answer:**
```python
names = ["  ada  ", "  grace ", " betty "]
clean_names = list(map(lambda name: name.strip().capitalize(), names))
# Result: ['Ada', 'Grace', 'Betty']
```

### Using filter

### 12. **Difficulty: Intermediate**
Given the list `numbers = list(range(1, 21))`, use `filter` and a lambda function to create a new list containing only the numbers divisible by both 2 and 3.

**Answer:**
```python
numbers = list(range(1, 21))
divisible_by_6 = list(filter(lambda x: x % 2 == 0 and x % 3 == 0, numbers))
# Result: [6, 12, 18]
```

### 13. **Difficulty: Intermediate**
Given the list `words = ['apple', 'banana', 'kiwi', 'orange', 'grape']`, use `filter` and a lambda function to create a list of words that have more than 5 letters.

**Answer:**
```python
words = ['apple', 'banana', 'kiwi', 'orange', 'grape']
long_words = list(filter(lambda word: len(word) > 5, words))
# Result: ['banana', 'orange']
```

### 14. **Difficulty: Intermediate**
Given a list of mixed data types `data = [0, "hello", None, 5.5, True, "world", False]`, use `filter` and a lambda function to create a list that excludes all falsy values.

**Answer:**
```python
data = [0, "hello", None, 5.5, True, "world", False]
truthy_values = list(filter(lambda x: x, data))
# Result: ['hello', 5.5, True, 'world']
```

### Using sorted

### 15. **Difficulty: Intermediate**
Given `people = [('John', 28), ('Jane', 22), ('Dave', 35)]`, sort the list of tuples by age (the second element) in descending order using `sorted` and a lambda function.

**Answer:**
```python
people = [('John', 28), ('Jane', 22), ('Dave', 35)]
sorted_by_age = sorted(people, key=lambda person: person[1], reverse=True)
# Result: [('Dave', 35), ('John', 28), ('Jane', 22)]
```

### 16. **Difficulty: Advanced**
Given a list of dictionaries `products = [{'name': 'Laptop', 'price': 1200}, {'name': 'Mouse', 'price': 25}, {'name': 'Keyboard', 'price': 75}]`, sort the list by the length of the product's name, from shortest to longest.

**Answer:**
```python
products = [{'name': 'Laptop', 'price': 1200}, {'name': 'Mouse', 'price': 25}, {'name': 'Keyboard', 'price': 75}]
sorted_by_name_length = sorted(products, key=lambda product: len(product['name']))
# Result: [{'name': 'Mouse', 'price': 25}, {'name': 'Laptop', 'price': 1200}, {'name': 'Keyboard', 'price': 75}]
```

### 17. **Difficulty: Advanced**
Given the list `scores = [('Alice', 88, 92), ('Bob', 76, 81), ('Charlie', 95, 89)]`, sort the list based on the average of the two scores for each student (the second and third elements of the tuple) in descending order.

**Answer:**
```python
scores = [('Alice', 88, 92), ('Bob', 76, 81), ('Charlie', 95, 89)]
sorted_by_average = sorted(scores, key=lambda student: (student[1] + student[2]) / 2, reverse=True)
# Result: [('Charlie', 95, 89), ('Alice', 88, 92), ('Bob', 76, 81)]
```

### Using reduce

For the following questions, assume you have access to a reduce function as implemented in the PY130 exercises:

```python
def reduce(callback, iterable, start):
    accum = start
    for item in iterable:
        accum = callback(item, accum)
    return accum
```

### 18. **Difficulty: Intermediate**
Given `numbers = (1, 2, 4, 8, 16)`, use the provided `reduce` function and a lambda to compute the sum of all numbers, starting with an accumulator value of 0.

**Answer:**
```python
numbers = (1, 2, 4, 8, 16)
total = reduce(lambda num, accum: num + accum, numbers, 0)
# Result: 31
```

### 19. **Difficulty: Intermediate**
Using the `reduce` function and `numbers = [10, 3, 5]`, write a lambda to compute the product of all numbers, starting with an initial accumulator value of 1.

**Answer:**
```python
numbers = [10, 3, 5]
product = reduce(lambda num, accum: num * accum, numbers, 1)
# Result: 150
```

### 20. **Difficulty: Advanced**
Using the `reduce` function, find the character that appears earliest in alphabetical order from the list `colors = ['red', 'orange', 'yellow', 'green', 'blue']`. Your lambda should compare the first letter of each color to the accumulator. Start with an initial accumulator value of 'z'.

**Answer:**
```python
colors = ['red', 'orange', 'yellow', 'green', 'blue']
earliest_char = reduce(lambda color, accum: color[0] if color[0] < accum else accum, colors, 'z')
# Result: 'b' (from 'blue')
```