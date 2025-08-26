# Python Function Arguments - Practice Problems with Solutions

## 1. **Intermediate**: Basic Positional Arguments

Write a function named `combine` that takes three positional arguments and returns a tuple containing all three. Call this function with three different values.

### Solution:

```python
def combine(arg1, arg2, arg3):
    """
    Takes three positional arguments and returns them as a tuple.
    """
    return (arg1, arg2, arg3)

# Example usage:
result = combine("hello", 42, True)
print(result)  # Output: ('hello', 42, True)

# More examples:
print(combine(1, 2, 3))           # Output: (1, 2, 3)
print(combine("a", "b", "c"))     # Output: ('a', 'b', 'c')
print(combine([1, 2], {3, 4}, (5, 6)))  # Output: ([1, 2], {3, 4}, (5, 6))
```

---

## 2. **Intermediate**: Positional-Only Arguments

Define a function named `multiply` that accepts two positional-only arguments and returns their product. The function should not allow these parameters to be passed as keyword arguments.

### Solution:

```python
def multiply(a, b, /):
    """
    Multiplies two numbers using positional-only arguments.
    The '/' syntax ensures arguments can only be passed positionally.
    """
    return a * b

# Example usage:
result = multiply(5, 3)
print(result)  # Output: 15

print(multiply(2.5, 4))    # Output: 10.0
print(multiply(-3, 7))     # Output: -21

# This would raise a TypeError:
# multiply(a=5, b=3)  # TypeError: multiply() got some positional-only arguments passed as keyword arguments
```

---

## 3. **Intermediate**: Mixed Positional and Keyword Arguments with Restrictions

Create a function named `describe_pet` that takes one positional argument `animal_type` and one keyword argument `name` with a default value of an empty string. The function should print a description of the pet. The function should not accept more than 1 positional argument.

### Solution:

```python
def describe_pet(animal_type, /, *, name=""):
    """
    Describes a pet with one positional-only argument and one keyword-only argument.
    animal_type: positional-only argument
    name: keyword-only argument with default empty string
    """
    if name:
        print(f"I have a {animal_type} named {name}.")
    else:
        print(f"I have a {animal_type}.")

# Example usage:
describe_pet("dog")                    # Output: I have a dog.
describe_pet("cat", name="Whiskers")   # Output: I have a cat named Whiskers.
describe_pet("bird", name="Tweety")    # Output: I have a bird named Tweety.

# These would raise TypeErrors:
# describe_pet("dog", "Buddy")          # Too many positional arguments
# describe_pet(animal_type="dog")       # animal_type must be positional
```

---

## 4. **Intermediate**: Variable Number of Arguments (*args)

Write a function named `calculate_average` that accepts any number of numeric arguments and returns their average. Make sure it returns `None` if no arguments are provided.

### Solution:

```python
def calculate_average(*numbers):
    """
    Calculates the average of any number of numeric arguments.
    Returns None if no arguments are provided.
    """
    if not numbers:
        return None
    
    return sum(numbers) / len(numbers)

# Example usage:
print(calculate_average())              # Output: None
print(calculate_average(10))            # Output: 10.0
print(calculate_average(1, 2, 3, 4, 5)) # Output: 3.0
print(calculate_average(2.5, 7.5))      # Output: 5.0
print(calculate_average(-1, 0, 1))      # Output: 0.0
```

### Alternative Solution with Type Checking:

```python
def calculate_average(*numbers):
    """
    Enhanced version with ba