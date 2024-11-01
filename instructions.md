# Week 11 Discussion - Function and Class Design

This discussion covers two programming and software design concepts:

* The Single Responsibility Principle
* DRY code (**D**on't **R**epeat **Y**ourself)

## Single Responsibility Principle

A common "beginner mistake" in programming is overloading both functions and classes so that a single function or class does many things.
However, this is a violation of a software design best practice called the "single resonsibility principle".
In software design, the "Single Responsibility Principle" is the idea that a function or class should have one single responsibility.
The single responsibility principle is part of a larger guideline called [SOLID](https://www.digitalocean.com/community/conceptual-articles/s-o-l-i-d-the-first-five-principles-of-object-oriented-design#single-responsibility-principle), which gives guidelines for object oriented design.

As a simple example, consider this function:

```python
def square_and_is_even(num):
    # Calculate square
    squared_value = num * num

    # Check if even
    even = squared_value % 2 == 0

    return squared_value, even

result = square_and_is_even(5)
print(f"Squared Value: {result[0]}, Is Even: {result[1]}")
```

In the code above, the function has two tasks. 
It would be better to separate this into two functions:

```python
def square(num):
    return num * num

def is_even(value):
    return value % 2 == 0

number = 5
squared_value = square(number)
even_check = is_even(squared_value)

print(f"Squared Value: {squared_value}, Is Even: {even_check}")
```

## DRY Code

DRY code stands for "Don't Repeat Yourself" and promotes reusability and maintainability. 
It eliminates redundancy and ensures that changes only need to be made in one place.

Consider the example below, the file reading should be put into a function

```python
with open("simulationA.txt", "r") as file:
    for line in file:
        if "energy:" in line:
            energy_a = line.split(":")[1].strip()
            print(f"Energy from simulationA: {energy_a}")

with open("simulationB.txt", "r") as file:
    for line in file:
        if "energy:" in line:
            energy_b = line.split(":")[1].strip()
            print(f"Energy from simulationB: {energy_b}")
```

## Part 1: Function Design

For this portion of the discussion, you are provided with some code in the module `function_design.py`. 
The code in this module carries out multiple tasks related to a molecule based on its XYZ file

1. **Identification**: Consider the provided function - identify the tasks or responsibilities the current function is handling. 

2. **Discussion on Separation**: 
    - How might you break down the function into smaller, more focused functions?
    - What are the potential benefits of such a separation? For example, is it easier to divide work there is one function per task? Do you anticipate that such code could be easier to maintain?
    - Are there any challenges or disadvantages to separating responsibilities?

3. Where is the **DRY** principle violated? How might you fix this?

4. **Consideration on Data Structures**: 
    - How does the use of data structures (like dictionaries vs if-else chains) impact the readability and maintainability of the code? Consider the `if` statements - is there a more "clean" way to do this using a Python data structure that we've learned about?

5. **File Path Construction**: Reflect on how the function constructs the file path from the molecule name. What are the implications in terms of code flexibility? What if someone has a file that is in a different location or is named something different?

After you have considered these questions, write an improved module that addresses the single responsibility principle and DRY code. 
Create a new file for your implementation, keeping the original "bad" version so you can directly compare them.
Is your new version easier to read or maintain? Hint: It should be :) Why?

**Report Out** on the shared slides on the approach your group took.

## Part 2: Class Design

You are provided with a molecule class in the Python module `class_design.py`. 
Your task for this part is to evaluate and rewrite this class.

### Discussion
1. Is there anywhere SRP or DRY principles are violated in this class? If so, how would you fix it?

2. When designing a Python class, you should also try to make the class "Pythonic".
The use of `get_something` and `set_something` in a Python class is [considered to be an anti-pattern](https://docs.quantifiedcode.com/python-anti-patterns/correctness/implementing_java-style_getters_and_setters.html).
Identify places where `@property` should be used instead. Make a modified version of the class and demonstrate its use in another Python module.

3. How would this class be written differently in C++? 

**Report Out** on the shared slides on the approach your group took.

