# Python Closures and Partial Functions - Practice Problems with Solutions

## 1. **Intermediate**: Closure Variable Access

What will the following code print?

```python
def make_greeting():
    greeting = "Hello"

    def greet_func(name, greet=None):
        if not greet:
            return f"{greeting} {name}!"

        return f"{greet} {name}!"

    return greet_func

greet_person = make_greeting()
print(greet_person("John", "Goodbye"))
print(greet_person("Jane"))
```

### Answer:
```
Goodbye John!
Hello Jane!
```

**Explanation:**
- First call: `greet` parameter is "Goodbye", so it uses the provided greeting
- Second call: `greet` parameter is None (default), so it uses the closed-over `greeting` variable "Hello"

---

## 2. **Intermediate**: Counter Without State Persistence

What does the following program print? Try to answer without running the code.

```python
def make_counter():
    def counter_func():
        counter = 0
        counter += 1
        return counter

    return counter_func

increment_counter = make_counter()
print(increment_counter())
print(increment_counter())

increment_counter = make_counter()
print(increment_counter())
print(increment_counter())
```

### Answer:
```
1
1
1
1
```

**Explanation:**
The `counter` variable is reinitialized to 0 every time `counter_func()` is called, so it always returns 1. The variable is not closed over from the outer scope, so state is not preserved between calls.

---

## 3. **Basic**: Partial Function Application

What will this code print? Try to answer without running the code.

```python
from functools import partial

def greet(name, greeting):
    return f"{greeting}, {name}!"

say_hello_to = partial(greet, greeting="Hello")
print(say_hello_to(name="Alice"))
```

### Answer:
```
Hello, Alice!
```

**Explanation:**
`partial` creates a new function with the `greeting` argument pre-filled with "Hello". When called with `name="Alice"`, it calls `greet("Alice", "Hello")`.

---

## 4. **Basic**: Simple Function Factory

Write a function named `later` that takes two arguments: a function, `func`, and an argument for that function, `argument`. The return value should be a new function that calls `func` with `argument` as its argument.

```python
# Example usage:
def printer(message):
    print(message)

print_warning = later(printer, "The system is shutting down!")
print_warning()  # Expected output: The system is shutting down!
```

### Solution:

```python
def later(func, argument):
    """
    Returns a new function that calls func with the pre-specified argument.
    """
    def new_function():
        return func(argument)
    return new_function

# Example usage:
def printer(message):
    print(message)

print_warning = later(printer, "The system is shutting down!")
print_warning()  # Output: The system is shutting down!

# More examples:
def multiply_by_two(x):
    return x * 2

double_five = later(multiply_by_two, 5)
print(double_five())  # Output: 10
```

---

## 5. **Intermediate**: Two-Argument Function Factory

Write a function named `later2` that takes two arguments: a function, `func`, and an argument for that function, `first_arg`. The return value should be a new function that takes an argument, `second_arg`. The new function should call `func` with the arguments provided by `first_arg` and `second_arg`.

```python
# Example usage:
def notify(message, when):
    print(f"{message} in {when} minutes!")

shutdown_warning = later2(notify, "The system is shutting down")
shutdown_warning(30) # Expected output: The system is shutting down in 30 minutes!
```

### Solution:

```python
def later2(func, first_arg):
    """
    Returns a new function that takes a second argument and calls func
    with both the pre-specified first argument and the new second argument.
    """
    def new_function(second_arg):
        return func(first_arg, second_arg)
    return new_function

# Example usage:
def notify(message, when):
    print(f"{message} in {when} minutes!")

shutdown_warning = later2(notify, "The system is shutting down")
shutdown_warning(30)  # Output: The system is shutting down in 30 minutes!

# More examples:
def add(x, y):
    return x + y

add_five = later2(add, 5)
print(add_five(3))  # Output: 8
print(add_five(10)) # Output: 15
```

---

## 6. **Basic**: Simple Closure

What will the following code print?

```python
def make_adder(x):
    def add(y):
        return x + y
    return add

add5 = make_adder(5)
print(add5(10))
print(add5(20))
```

### Answer:
```
15
25
```

**Explanation:**
`make_adder(5)` creates a closure where `x` is bound to 5. The returned `add` function remembers this value and adds it to whatever `y` is passed to it.

---

## 7. **Advanced**: Late Binding Closure Problem

What will the following code print? Explain the behavior.

```python
adders = []
for n in range(1, 4):
    adders.append(lambda x: n + x)

add1, add2, add3 = adders

print(add1(10))
print(add2(10))
print(add3(10))
```

### Answer:
```
13
13
13
```

**Explanation:**
This is the classic "late binding closure" problem. All lambda functions capture the same variable `n` by reference, not by value. When the loop completes, `n` has the value 3, so all lambda functions use 3 when called. The variable `n` is resolved at call time, not at definition time.

---

## 8. **Advanced**: Fixing Late Binding Closure

The code from the previous question does not behave as one might initially expect. How can you modify the lambda function to produce the expected output of 11, 12, and 13?

### Solutions:

**Solution 1: Using Default Parameter**
```python
adders = []
for n in range(1, 4):
    adders.append(lambda x, n=n: n + x)

add1, add2, add3 = adders
print(add1(10))  # Output: 11
print(add2(10))  # Output: 12
print(add3(10))  # Output: 13
```

**Solution 2: Using a Factory Function**
```python
def make_adder(n):
    return lambda x: n + x

adders = []
for n in range(1, 4):
    adders.append(make_adder(n))

add1, add2, add3 = adders
print(add1(10))  # Output: 11
print(add2(10))  # Output: 12
print(add3(10))  # Output: 13
```

**Solution 3: Using Partial**
```python
from functools import partial

def add(n, x):
    return n + x

adders = []
for n in range(1, 4):
    adders.append(partial(add, n))

add1, add2, add3 = adders
print(add1(10))  # Output: 11
print(add2(10))  # Output: 12
print(add3(10))  # Output: 13
```

---

## 9. **Basic**: Definition of Closure

In your own words, what is a closure in Python? What are its essential characteristics?

### Answer:

A **closure** in Python is a function that has access to variables from an outer (enclosing) scope even after the outer function has finished executing. 

**Essential characteristics:**
1. **Nested Function**: A closure involves a function defined inside another function
2. **Access to Outer Variables**: The inner function can access variables from the outer function's scope
3. **Persistence**: The outer function's variables remain accessible even after the outer function returns
4. **State Preservation**: Each closure maintains its own copy of the outer function's variables

**Example:**
```python
def outer_function(x):
    # This variable will be "closed over"
    outer_var = x
    
    def inner_function(y):
        # This function can access outer_var
        return outer_var + y
    
    return inner_function  # Returns the closure

# outer_function has finished, but outer_var is still accessible
my_closure = outer_function(10)
print(my_closure(5))  # Output: 15
```

---

## 10. **Basic**: Free Variables

What is a "free variable" in the context of a closure?

### Answer:

A **free variable** is a variable that is used inside a function but is not defined locally within that function, nor is it a parameter of that function. Instead, it's defined in an outer (enclosing) scope.

In closures, free variables are the variables from the outer function that the inner function "closes over" or captures.

**Example:**
```python
def make_multiplier(factor):
    # 'factor' is a parameter of the outer function
    
    def multiply(number):
        # 'factor' is a free variable in this inner function
        # It's not defined locally, nor is it a parameter of multiply()
        # It comes from the enclosing scope
        return factor * number
    
    return multiply

times_3 = make_multiplier(3)
# The closure 'times_3' has captured the free variable 'factor' with value 3
```

In this example, `factor` is a free variable in the `multiply` function because it's referenced but not defined within `multiply`'s local scope.

---

## 11. **Basic**: Multiplier Factory

Write a factory function `make_multiplier(n)` that returns a function. The returned function should take one argument `x` and return the product of `n` and `x`.

```python
# Example usage:
times_3 = make_multiplier(3)
print(times_3(5))  # Expected output: 15

times_10 = make_multiplier(10)
print(times_10(5)) # Expected output: 50
```

### Solution:

```python
def make_multiplier(n):
    """
    Factory function that returns a multiplier function.
    The returned function multiplies its argument by n.
    """
    def multiplier(x):
        return n * x
    return multiplier

# Example usage:
times_3 = make_multiplier(3)
print(times_3(5))   # Output: 15
print(times_3(10))  # Output: 30

times_10 = make_multiplier(10)
print(times_10(5))  # Output: 50
print(times_10(7))  # Output: 70

# Each closure maintains its own 'n' value
print(times_3(2))   # Output: 6 (still uses n=3)
print(times_10(2))  # Output: 20 (still uses n=10)
```

---

## 12. **Intermediate**: Loop Variable Closure Problem

The following code is intended to create a list of functions, where each function prints its creation index (0, 1, 2). However, it prints 2 three times. Explain why this happens and provide a corrected version of the code.

```python
funcs = []
for i in range(3):
    def print_i():
        print(i)
    funcs.append(print_i)

for f in funcs:
    f()
```

### Problem Explanation:
This code prints `2` three times because all functions share the same variable `i` by reference. When the loop completes, `i` has the value 2, and all functions print this final value.

### Corrected Solutions:

**Solution 1: Using Default Parameter**
```python
funcs = []
for i in range(3):
    def print_i(index=i):  # Capture i's current value as default parameter
        print(index)
    funcs.append(print_i)

for f in funcs:
    f()
# Output: 0, 1, 2
```

**Solution 2: Using a Factory Function**
```python
def make_printer(index):
    def print_index():
        print(index)
    return print_index

funcs = []
for i in range(3):
    funcs.append(make_printer(i))

for f in funcs:
    f()
# Output: 0, 1, 2
```

**Solution 3: Using Lambda with Default Parameter**
```python
funcs = []
for i in range(3):
    funcs.append(lambda index=i: print(index))

for f in funcs:
    f()
# Output: 0, 1, 2
```

---

## 13. **Intermediate**: Mutable State in Closure

What will the following code print? Explain how the closure maintains state.

```python
def make_counter():
    count = [0]
    def counter():
        count[0] += 1
        return count[0]
    return counter

counter1 = make_counter()
print(counter1())
print(counter1())

counter2 = make_counter()
print(counter2())
print(counter1())
```

### Answer:
```
1
2
1
3
```

**Explanation:**
- The closure uses a mutable object (list) to maintain state
- Each call to `make_counter()` creates a new list `[0]`
- `counter1` and `counter2` each have their own separate `count` list
- When `counter1()` is called, it modifies its own `count[0]`
- When `counter2()` is called, it modifies its own separate `count[0]`
- The state persists between calls because the list object is closed over

---

## 14. **Advanced**: Assignment to Free Variable Error

What happens when you run the following code and call `bad_counter()`? Explain the error that occurs.

```python
def make_bad_counter():
    count = 0
    def counter():
        count += 1
        return count
    return counter

bad_counter = make_bad_counter()
# bad_counter() # What happens here?
```

### Answer:

**Error:** `UnboundLocalError: local variable 'count' referenced before assignment`

**Explanation:**
When Python sees `count += 1`, it interprets this as `count = count + 1`, which means `count` is being assigned to. Python treats any variable that's assigned to in a function as a local variable. However, the right side `count + 1` tries to read `count` before it's been assigned locally, causing the error.

The assignment operation makes Python treat `count` as local to the `counter` function, so it doesn't look in the enclosing scope for the variable.

---

## 15. **Advanced**: Using nonlocal

Explain the purpose of the `nonlocal` keyword. Rewrite the `make_bad_counter` function from the previous question using `nonlocal` so that it works as an incrementing counter.

### Explanation of nonlocal:

The `nonlocal` keyword allows a nested function to modify variables in the nearest enclosing scope that is not global. It tells Python that the variable is not local to the current function, but exists in an outer function's scope.

### Solution:

```python
def make_counter():
    count = 0
    def counter():
        nonlocal count  # This tells Python to use the count from the outer scope
        count += 1
        return count
    return counter

# Example usage:
good_counter = make_counter()
print(good_counter())  # Output: 1
print(good_counter())  # Output: 2
print(good_counter())  # Output: 3

# Each counter maintains its own state
another_counter = make_counter()
print(another_counter())  # Output: 1
print(good_counter())     # Output: 4
```

**Alternative Solution without nonlocal (using mutable container):**
```python
def make_counter():
    count = [0]  # Use a mutable container
    def counter():
        count[0] += 1  # Modify the container's contents, not the variable itself
        return count[0]
    return counter
```

---

## 16. **Intermediate**: Password Protection Function

Write a function `password_protected(password)` that takes a password string. It should return a new function that takes one argument. If the argument matches the original password, the returned function should return `True`. Otherwise, it should return `False`.

```python
# Example usage:
is_correct_password = password_protected("p@ssword123")
print(is_correct_password("wrong_password")) # Expected: False
print(is_correct_password("p@ssword123"))   # Expected: True
```

### Solution:

```python
def password_protected(password):
    """
    Returns a function that checks if a given input matches the stored password.
    """
    def check_password(input_password):
        return input_password == password
    return check_password

# Example usage:
is_correct_password = password_protected("p@ssword123")
print(is_correct_password("wrong_password"))  # Output: False
print(is_correct_password("p@ssword123"))     # Output: True
print(is_correct_password("PASSWORD123"))     # Output: False (case sensitive)

# Multiple password checkers
admin_check = password_protected("admin123")
user_check = password_protected("user456")

print(admin_check("admin123"))  # Output: True
print(admin_check("user456"))   # Output: False
print(user_check("user456"))    # Output: True
```

### Enhanced Solution with Additional Features:

```python
def password_protected(password, max_attempts=3):
    """
    Enhanced version with attempt limiting.
    """
    attempts = [0]  # Use list for mutable state
    
    def check_password(input_password):
        if attempts[0] >= max_attempts:
            return "Account locked"
        
        if input_password == password:
            attempts[0] = 0  # Reset attempts on successful login
            return True
        else:
            attempts[0] += 1
            return False
    
    return check_password
```

---

## 17. **Basic**: Multiple Closures with Different Values

What will this code print?

```python
def outer_func(x):
    y = 4
    def inner_func(z):
        return x + y + z
    return inner_func

closure1 = outer_func(10)
closure2 = outer_func(20)

print(closure1(1))
print(closure2(1))
```

### Answer:
```
15
25
```

**Explanation:**
- `closure1` captures `x=10` and `y=4`, so `closure1(1)` returns `10 + 4 + 1 = 15`
- `closure2` captures `x=20` and `y=4`, so `closure2(1)` returns `20 + 4 + 1 = 25`
- Each closure maintains its own copy of the outer function's variables

---

## 18. **Advanced**: Running Average Calculator

Write a function `running_average()` that returns a new function. The returned function, when called with a number, should return the running average of all numbers passed to it since it was created.

```python
# Example usage:
avg_calculator = running_average()
print(avg_calculator(10)) # Expected: 10.0
print(avg_calculator(20)) # Expected: 15.0
print(avg_calculator(30)) # Expected: 20.0

avg_calculator2 = running_average()
print(avg_calculator2(5)) # Expected: 5.0
```

### Solution:

```python
def running_average():
    """
    Returns a function that calculates the running average of all numbers passed to it.
    """
    numbers = []
    
    def add_number(num):
        numbers.append(num)
        return sum(numbers) / len(numbers)
    
    return add_number

# Example usage:
avg_calculator = running_average()
print(avg_calculator(10))  # Output: 10.0
print(avg_calculator(20))  # Output: 15.0
print(avg_calculator(30))  # Output: 20.0

avg_calculator2 = running_average()
print(avg_calculator2(5))  # Output: 5.0
print(avg_calculator2(15)) # Output: 10.0

# Original calculator still maintains its own state
print(avg_calculator(40))  # Output: 25.0 (10+20+30+40)/4
```

### Alternative Solution (More Memory Efficient):

```python
def running_average():
    """
    Memory-efficient version that tracks count and sum instead of all numbers.
    """
    state = {'count': 0, 'total': 0}
    
    def add_number(num):
        state['count'] += 1
        state['total'] += num
        return state['total'] / state['count']
    
    return add_number
```

---

## 19. **Intermediate**: Closures vs functools.partial

What is the difference between using a closure and `functools.partial` to achieve partial function application? When might you prefer one over the other?

### Answer:

**Closures:**
- **Flexibility**: Can contain complex logic, conditionals, and state management
- **State**: Can maintain mutable state between calls
- **Multiple Operations**: Can perform multiple operations or transformations
- **Dynamic Behavior**: Can modify behavior based on closure variables

**functools.partial:**
- **Simplicity**: Cleaner syntax for simple argument fixing
- **Performance**: Slightly more efficient for simple cases
- **Immutable**: Creates a new function with fixed arguments
- **Introspection**: Provides `func`, `args`, and `keywords` attributes

### When to Use Each:

**Use Closures when:**
```python
# Complex logic or state management
def make_validator(min_length, max_length):
    def validate(password):
        if len(password) < min_length:
            return f"Password too short (min {min_length})"
        if len(password) > max_length:
            return f"Password too long (max {max_length})"
        return "Valid password"
    return validate

# Maintaining state
def make_counter():
    count = 0
    def increment():
        nonlocal count
        count += 1
        return count
    return increment
```

**Use functools.partial when:**
```python
from functools import partial

# Simple argument fixing
def multiply(x, y):
    return x * y

double = partial(multiply, 2)  # Cleaner than lambda x: multiply(2, x)

# Working with existing functions
from operator import add
add_five = partial(add, 5)
```

---

## 20. **Basic**: Partial with Keyword Arguments

What does the following code print?

```python
from functools import partial

def power(base, exponent):
    return base ** exponent

square = partial(power, exponent=2)
cube = partial(power, exponent=3)

prin