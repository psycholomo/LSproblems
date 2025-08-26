# Python First-Class Functions and Higher-Order Functions Study Guide

## Basic Questions

### 1. Basic: In the context of Python, what are the three conditions an object must meet to be considered a "first-class citizen"?

can be passed as an arugment to a funciton, can be stored as a value, can be returned in a function

**Answer:**
An object must meet these three conditions to be considered a first-class citizen:
1. **Can be passed as an argument** to a function
2. **Can be returned as a value** from a function
3. **Can be assigned to a variable** (and stored in data structures)

### 2. Basic: Define what a "higher-order function" is in Python. Provide the two criteria that a function must meet to be classified as such.

a higher ordre function takes a function as an argument and can return a function

**Answer:**
A higher-order function is a function that operates on other functions. It must meet at least one of these criteria:
1. **Takes one or more functions as arguments**, OR
2. **Returns a function as its result**

### 3. Basic: Explain the difference between a first-class function and a higher-order function. Can a function be one without being the other?

the main different is a higher-order function is used with closure to keep track of state. Where a first class function is used as a value. and is treated like a value

**Answer:**
- **First-class function**: A function that can be treated like any other object (passed around, assigned to variables, etc.)
- **Higher-order function**: A function that either takes functions as arguments or returns functions

**Yes, a function can be one without being the other:**
- All functions in Python are first-class objects by default
- But not all functions are higher-order functions (only those that take or return functions)
- Example: `def add(x, y): return x + y` is first-class but not higher-order

### 4. Basic: What is a "callback function"? Write a simple example of a higher-order function that uses a callback.

a callback function is a function passed in as an argument to another function and called

def process_numbers(numbers, callback):

    for num in numbers:
        callback(num)
        

**Answer:**
A **callback function** is a function that is passed as an argument to another function and is called (invoked) within that function.

```python
def process_numbers(numbers, callback):
    result = []
    for num in numbers:
        result.append(callback(num))
    return result

def square(x):
    return x ** 2

# square is the callback function
numbers = [1, 2, 3, 4]
squared = process_numbers(numbers, square)
print(squared)  # [1, 4, 9, 16]
```

### 5. Basic: All functions in Python are first-class objects. Does this mean all functions are also higher-order functions? Explain your reasoning.

**Answer:**
**No.** While all functions in Python are first-class objects, not all functions are higher-order functions.

- **First-class**: Functions can be assigned to variables, passed as arguments, etc.
- **Higher-order**: Functions must either take functions as arguments OR return functions

Example of a first-class function that is NOT higher-order:
```python
def add(x, y):
    return x + y

# This is first-class (can be assigned, passed around)
# But NOT higher-order (doesn't take or return functions)
```

## Intermediate Questions

### 6. Intermediate: Using the refined definition from the PY130 course material, explain why the built-in print function is not considered a true higher-order function, even though you can pass a function object to it as an argument.

**Answer:**
The `print` function is not considered a true higher-order function because:

1. **It doesn't operate ON the function** - it treats the function object like any other object
2. **It doesn't invoke/call the function** - it just prints the function's string representation
3. **True higher-order functions** are designed to work with functions as functional units, not just as objects

Example:
```python
def my_func():
    return "hello"

print(my_func)  # Prints: <function my_func at 0x...>
# print doesn't call my_func or use it functionally
```

### 7. Intermediate: What will the following code output? Explain how functions as first-class objects enable this behavior.

```python
def double(n):
    return n * 2

def triple(n):
    return n * 3

operation = double
print(operation(5))

operation = triple
print(operation(5))
```

**Answer:**
**Output:**
```
10
15
```

**Explanation:**
Functions as first-class objects enable this behavior because:
1. Functions can be **assigned to variables** (like `operation`)
2. The variable `operation` holds a **reference** to the function object
3. We can **call the function** through the variable using `operation(5)`
4. When we reassign `operation = triple`, it now points to the `triple` function
5. This enables **dynamic function assignment** at runtime

### 8. Intermediate: Write a lambda function that accepts a string and returns its uppercase version. Then, use the built-in map function and your lambda to transform a list of strings to uppercase.

```python
value = lambda x : x.upper()
return_value = map(value, a_list)

print(list(return_value))
```
**Answer:**
```python
# Lambda function
uppercase = lambda s: s.upper()

# Using with map
strings = ["hello", "world", "python"]
uppercase_strings = list(map(lambda s: s.upper(), strings))
print(uppercase_strings)  # ['HELLO', 'WORLD', 'PYTHON']

# Alternative using the named lambda
uppercase_strings2 = list(map(uppercase, strings))
print(uppercase_strings2)  # ['HELLO', 'WORLD', 'PYTHON']
```

### 9. Intermediate: What is the output of the following code? Explain the roles of create_greeter and hello in this example.

```python
def create_greeter(greeting):
    def hello(name):
        return f"{greeting}, {name}!"
    return hello

say_hi = create_greeter("Hi")
say_hola = create_greeter("Hola")

print(say_hi("Alice"))
print(say_hola("Bob"))
```

**Answer:**
**Output:**
```
Hi, Alice!
Hola, Bob!
```

**Explanation of roles:**
- **`create_greeter`**: Higher-order function that returns a function. It's a "factory" that creates customized greeting functions
- **`hello`**: Inner function (closure) that captures the `greeting` parameter from its enclosing scope
- **`say_hi` and `say_hola`**: Variables that hold the returned `hello` functions, each with different captured `greeting` values
- This demonstrates **closures** - the inner function remembers the environment in which it was created

### 10. Intermediate: Given the list numbers = [1, 2, 3, 4, 5, 6], use the built-in filter function with a lambda to create a new list containing only the even numbers.


**Answer:**
```python
numbers = [1, 2, 3, 4, 5, 6]
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(even_numbers)  # [2, 4, 6]

```

### 11. Intermediate: Refactor your solution from the previous question to use a list comprehension instead of filter.


**Answer:**
```python
numbers = [1, 2, 3, 4, 5, 6]
even_numbers = [x for x in numbers if x % 2 == 0]
print(even_numbers)  # [2, 4, 6]
```

### 12. Intermediate: What will the following code output? Explain how the key argument in the sorted function works.

```python
people = [
    {'name': 'Alice', 'age': 30},
    {'name': 'Bob', 'age': 25},
    {'name': 'Charlie', 'age': 35}
]

sorted_by_age = sorted(people, key=lambda person: person['age'])
print(sorted_by_age)
```

**Answer:**
**Output:**
```python
[{'name': 'Bob', 'age': 25}, {'name': 'Alice', 'age': 30}, {'name': 'Charlie', 'age': 35}]
```

**Explanation:**
The `key` argument in `sorted()` works as follows:
1. **Takes a function** that extracts a comparison key from each element
2. **Applies the key function** to each item in the list
3. **Sorts based on the returned values** rather than the original objects
4. In this case, `lambda person: person['age']` extracts the 'age' value
5. The list is sorted by age values: 25, 30, 35

### 13. Intermediate: Write a function execute_operations that takes a list of functions and a starting value. The function should apply each function in the list sequentially to the value.

operations_list = [lambda x: x + 1, lambda x: x * 2]
initial_value = 5

**Answer:**
```python
def execute_operations(functions, starting_value):
    result = starting_value
    for func in functions:
        result = func(result)
    return result

# Example usage:
operations = [lambda x: x + 1, lambda x: x * 2]
result = execute_operations(operations, 5)
print(result)  # 12 (5 + 1 = 6, then 6 * 2 = 12)

# Another example:
operations2 = [
    lambda x: x * 2,    # 5 * 2 = 10
    lambda x: x + 3,    # 10 + 3 = 13
    lambda x: x ** 2    # 13 ** 2 = 169
]
result2 = execute_operations(operations2, 5)
print(result2)  # 169
```

### 14. Intermediate: What does it mean that map and filter return a "lazy" sequence? How do you typically consume the results from these functions?

**Answer:**
**"Lazy" sequence means:**
1. **No immediate computation** - `map` and `filter` return iterator objects, not lists
2. **Values computed on-demand** - results are generated only when requested
3. **Memory efficient** - doesn't store all results in memory at once
4. **Single-pass iteration** - can only be consumed once

**How to consume the results:**
```python
numbers = [1, 2, 3, 4, 5]

# map returns an iterator
doubled = map(lambda x: x * 2, numbers)
print(type(doubled))  # <class 'map'>

# Ways to consume:
# 1. Convert to list
doubled_list = list(doubled)
print(doubled_list)  # [2, 4, 6, 8, 10]

# 2. Iterate directly
evens = filter(lambda x: x % 2 == 0, numbers)
for num in evens:
    print(num)  # 2, 4

# 3. Use next() for single items
squares = map(lambda x: x**2, numbers)
print(next(squares))  # 1
print(next(squares))  # 4
```

## Advanced Questions

### 15. Advanced: Write your own implementation of the map function called my_map.


**Answer:**
```python
def my_map(callback, iterable):
    result = []
    for item in iterable:
        result.append(callback(item))
    return result

# Example usage:
numbers = [1, 2, 3, 4, 5]
doubled = my_map(lambda x: x * 2, numbers)
print(doubled)  # [2, 4, 6, 8, 10]

# Test with strings
words = ["hello", "world"]
uppercase = my_map(str.upper, words)
print(uppercase)  # ['HELLO', 'WORLD']
```

### 16. Advanced: Write your own implementation of the filter function called my_filter.

**Answer:**
```python
def my_filter(callback, iterable):
    result = []
    for item in iterable:
        if callback(item):
            result.append(item)
    return result

# Example usage:
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
evens = my_filter(lambda x: x % 2 == 0, numbers)
print(evens)  # [2, 4, 6, 8, 10]

# Test with strings
words = ["apple", "banana", "apricot", "cherry"]
a_words = my_filter(lambda word: word.startswith('a'), words)
print(a_words)  # ['apple', 'apricot']
```

### 17. Advanced: Explain what is happening in the create_object function and predict the output.

```python
class Product:
    def __init__(self, name):
        self.name = name

class User:
    def __init__(self, name):
        self.name = name

def create_object(cls, name):
    obj = cls(name)
    return obj

p = create_object(Product, "Laptop")
u = create_object(User, "JohnDoe")

print(type(p), p.name)
print(type(u), u.name)
```

**Answer:**
**Output:**
```
<class '__main__.Product'> Laptop
<class '__main__.User'> JohnDoe
```

**Explanation:**
1. **Classes are first-class objects** in Python - they can be passed as arguments
2. **`create_object` is a factory function** that takes a class and arguments
3. **`cls(name)` calls the class constructor** - equivalent to `Product("Laptop")` or `User("JohnDoe")`
4. **Dynamic object creation** - the function can create instances of any class passed to it
5. This demonstrates that **classes themselves are objects** that can be manipulated like any other first-class object

### 18. Advanced: Write a higher-order function called negate that takes a predicate function and returns a new function that returns the logical opposite.
def negate(prediciate):
    def negated_prediciate(*args, **kwargs):
        return not predicate(*args, **kwargs)
    
    return negated_predicate


**Answer:**
```python
def negate(predicate):
    def negated_predicate(*args, **kwargs):
        return not predicate(*args, **kwargs)
    return negated_predicate

# Example usage:
def is_even(n):
    return n % 2 == 0

is_odd = negate(is_even)

print(is_odd(5))  # True (5 is odd, not even)
print(is_odd(4))  # False (4 is not odd, it's even)

# Additional examples:
def is_positive(n):
    return n > 0

is_not_positive = negate(is_positive)
print(is_not_positive(-5))  # True
print(is_not_positive(5))   # False

# Works with any predicate function
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
odd_numbers = list(filter(is_odd, numbers))
print(odd_numbers)  # [1, 3, 5, 7, 9]
```

### 19. Advanced: Write a higher-order function logged_call that takes a function func as an argument and returns a new function with logging.
def logged_call(func):
    def wrapper(*args, **kwargs):
        print(f'calling function {func.__name__})
        result = func(*args, **kwargs)
        return result
    return wrapper
**Answer:**
```python
def logged_call(func):
    def wrapper(*args, **kwargs):
        print(f"Calling function {func.__name__}")
        result = func(*args, **kwargs)
        print(f"Finished call to {func.__name__}")
        return result
    return wrapper

# Example usage:
def add(x, y):
    return x + y

def multiply(x, y):
    return x * y

# Create logged versions
logged_add = logged_call(add)
logged_multiply = logged_call(multiply)

# Test the functions
result1 = logged_add(3, 5)
print(f"Result: {result1}")
print()

result2 = logged_multiply(4, 6)
print(f"Result: {result2}")

# Output:
# Calling function add
# Finished call to add
# Result: 8
#
# Calling function multiply
# Finished call to multiply
# Result: 24
```

### 20. Advanced: Write a function compose that takes two functions, f and g, and returns a new function that represents f(g(x)).
def compose(f, g):
    def wrapper1(f,g):
        def wrapper2(g):

            return g
        return wrapper2(f + g)
    return wrapper1



**Answer:**
```python
def compose(f, g):
    def composed_function(x):
        return f(g(x))
    return composed_function

# Example usage:
def double(x):
    return x * 2
    
def add_one(x):
    return x + 1
    
double_then_add_one = compose(add_one, double)
print(double_then_add_one(5))  # 11 ((5 * 2) + 1)

# More examples:
def square(x):
    return x ** 2

def subtract_three(x):
    return x - 3

# Different compositions
square_then_subtract = compose(subtract_three, square)
subtract_then_square = compose(square, subtract_three)

print(square_then_subtract(5))   # 22 ((5^2) - 3 = 25 - 3)
print(subtract_then_square(5))   # 4  ((5 - 3)^2 = 2^2)

# Generic version that handles multiple arguments:
def compose_generic(f, g):
    def composed_function(*args, **kwargs):
        return f(g(*args, **kwargs))
    return composed_function
```

## Key Takeaways

1. **First-class functions** can be treated like any other object - assigned, passed, returned
2. **Higher-order functions** either take functions as arguments or return functions
3. **Closures** allow inner functions to capture variables from their enclosing scope
4. **Callbacks** enable flexible, reusable code by allowing functions to be customized
5. **Function composition** allows building complex operations from simple functions
6. Python's built-in functions like `map`, `filter`, and `sorted` are higher-order functions
7. **Lambda functions** provide a concise way to create simple functions inline