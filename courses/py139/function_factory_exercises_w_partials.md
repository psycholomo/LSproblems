# Python Function Factories - Practice Problems with Solutions

## 1. **Intermediate**: Partial Function Application

What will this code print? Try to answer without running the code:

```python
from functools import partial

def greet(name, greeting):
    return f"{greeting}, {name}!"

say_hello_to = partial(greet, greeting="Hello")
print(say_hello_to(name="Alice"))  # What will this print?
```

<details>
<summary>Solution</summary>

**Answer:** It prints `"Hello, Alice!"`

**Explanation:** The `partial` function from the `functools` module creates a new version of the `greet` function with the `greeting` argument pre-filled as `"Hello"`. Thus, when `say_hello_to` is called with `"Alice"` as the name, it completes the call by using the pre-set greeting.

</details>

---

## 2. **Intermediate**: Simple Function Factory

Write a function named `later` that takes two arguments: a function, `func`, and an argument for that function, `argument`. The return value should be a new function that calls `func` with `argument` as its argument. Here's an example of how it might be used:

```python
def printer(message):
    print(message)

print_warning = later(printer, "The system is shutting down!")
print_warning()  # The system is shutting down!
```

<details>
<summary>Solution</summary>

```python
def later(func, argument):
    def inner():
        return func(argument)

    return inner
```

**Alternative Solution with Lambda:**
```python
def later(func, argument):
    return lambda: func(argument)
```

**Example Usage:**
```python
def printer(message):
    print(message)

print_warning = later(printer, "The system is shutting down!")
print_warning()  # Output: The system is shutting down!

# More examples:
def multiply_by_two(x):
    return x * 2

double_five = later(multiply_by_two, 5)
print(double_five())  # Output: 10

def greet(name):
    return f"Hello, {name}!"

greet_alice = later(greet, "Alice")
print(greet_alice())  # Output: Hello, Alice!
```

</details>

---

## 3. **Intermediate**: Two-Argument Function Factory

Write a function named `later2` that takes two arguments: a function, `func`, and an argument for that function, `first_arg`. The return value should be a new function that takes an argument, `second_arg`. The new function should call the `func` with the arguments provided by `first_arg` and `second_arg`. Here's an example of how it might be used:

```python
def notify(message, when):
    print(f"{message} in {when} minutes!")

shutdown_warning = later2(notify, "The system is shutting down")
shutdown_warning(30) # The system is shutting down in 30 minutes!
```

<details>
<summary>Solution</summary>

```python
def later2(func, first_arg):
    def inner(second_arg):
        return func(first_arg, second_arg)

    return inner
```

**Alternative Solution with Lambda:**
```python
def later2(func, first_arg):
    return lambda second_arg: func(first_arg, second_arg)
```

**Example Usage:**
```python
def notify(message, when):
    print(f"{message} in {when} minutes!")

shutdown_warning = later2(notify, "The system is shutting down")
shutdown_warning(30)  # Output: The system is shutting down in 30 minutes!

# More examples:
def add(x, y):
    return x + y

add_five = later2(add, 5)
print(add_five(3))   # Output: 8
print(add_five(10))  # Output: 15

def power(base, exponent):
    return base ** exponent

square = later2(power, 2)  # Partial application for squaring
print(square(4))  # Output: 16
print(square(7))  # Output: 49

def format_message(template, value):
    return template.format(value)

error_formatter = later2(format_message, "Error: {}")
print(error_formatter("File not found"))  # Output: Error: File not found
```

**Comparison with functools.partial:**
```python
from functools import partial

# Using later2
shutdown_warning1 = later2(notify, "The system is shutting down")

# Using partial (equivalent functionality)
shutdown_warning2 = partial(notify, "The system is shutting down")

# Both work the same way:
shutdown_warning1(30)  # Output: The system is shutting down in 30 minutes!
shutdown_warning2(30)  # Output: The system is shutting down in 30 minutes!
```

</details>

---

## Additional Practice Problems

### 4. **Advanced**: Multiple Arguments Factory

Write a function named `later_n` that takes a function and any number of arguments, then returns a new function that takes the remaining arguments needed to complete the function call.

```python
def later_n(func, *args):
    def inner(*remaining_args):
        return func(*args, *remaining_args)
    return inner

# Example usage:
def calculate(a, b, c, d):
    return (a + b) * (c + d)

partial_calc = later_n(calculate, 1, 2)  # Pre-fill first two arguments
result = partial_calc(3, 4)  # Provide remaining arguments
print(result)  # Output: 21 (because (1+2) * (3+4) = 3 * 7 = 21)
```

### 5. **Advanced**: Configurable Factory

Write a function named `make_validator` that creates validation functions with different rules.

```python
def make_validator(min_length=0, max_length=float('inf'), required_chars=None):
    def validator(text):
        if len(text) < min_length:
            return f"Too short (minimum {min_length} characters)"
        if len(text) > max_length:
            return f"Too long (maximum {max_length} characters)"
        if required_chars:
            for char in required_chars:
                if char not in text:
                    return f"Missing required character: {char}"
        return "Valid"
    
    return validator

# Example usage:
password_validator = make_validator(min_length=8, max_length=20, required_chars='@#$')
username_validator = make_validator(min_length=3, max_length=15)

print(password_validator("abc"))           # Output: Too short (minimum 8 characters)
print(password_validator("validpass@#$"))  # Output: Valid
print(username_validator("bob"))           # Output: Valid
```

## Key Concepts Summary

### Function Factories vs Closures vs Partial

**Function Factories:**
- Create new functions dynamically
- Can encapsulate complex logic
- Maintain state through closures
- Highly flexible and customizable

**Closures:**
- Functions that capture variables from outer scope
- Maintain access to outer variables even after outer function returns
- Enable state preservation between calls

**functools.partial:**
- Built-in way to create partial functions
- Simpler syntax for basic argument pre-filling
- Less flexible than custom factories but more performant for simple cases

### When to Use Each Approach

**Use Function Factories when:**
- You need complex initialization logic
- You want to create multiple related functions
- You need to maintain mutable state
- You want maximum flexibility

**Use functools.partial when:**
- You simply need to pre-fill some arguments
- Working with existing functions you can't modify
- Performance is critical for simple operations
- You want cleaner, more readable code for basic cases