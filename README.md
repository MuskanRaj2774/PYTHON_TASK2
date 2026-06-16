# PYTHON_TASK2 – Decision Making & Functions in Python

* Conditional Statements
* Nested Conditions
* Multiple Conditions
* Logical Operators
* Functions
* Parameters
* Return Values
* Variable Scope
* Small Real-World Projects

---

# Topic 1 – Conditional Statements (if, else)

Conditional statements allow a program to make decisions.

Python checks a condition and executes code based on whether the condition is True or False.

### Syntax

```python
if condition:
    statement
else:
    statement
```

### Example

```python
age = 20

if age >= 18:
    print("Eligible")
else:
    print("Not Eligible")
```

### Programs Created

* Positive or Negative Number
* Voting Eligibility
* Even or Odd

---

# Topic 2 – Nested if Statements

Nested conditions mean placing one `if` statement inside another.

This is useful when a decision depends on multiple levels of checking.

### Syntax

```python
if condition1:
    if condition2:
        statement
```

### Example

```python
marks = 80
age = 18

if marks >= 70:
    if age >= 17:
        print("Eligible")
```

### Programs Created

* College Admission Eligibility
* ATM Withdrawal Validation
* Employee Bonus Eligibility

---

# Topic 3 – elif Statements

`elif` means **else if**.

Used when multiple conditions must be checked one after another.

### Syntax

```python
if condition:
    statement

elif condition:
    statement

else:
    statement
```

### Example

```python
marks = 85

if marks >= 90:
    print("A+")

elif marks >= 75:
    print("A")

else:
    print("B")
```

### Programs Created

* Grade Classification
* Traffic Signal
* Weather Recommendation

---

# Topic 4 – Logical Operators

Logical operators combine multiple conditions.

## and

Returns True only if both conditions are true.

```python
if age >= 18 and marks >= 80:
    print("Eligible")
```

## or

Returns True if one condition is true.

```python
if age >= 18 or marks >= 80:
    print("Eligible")
```

## not

Reverses condition result.

```python
if not False:
    print("True")
```

### Programs Created

* Login Validation
* Loan Eligibility
* Scholarship Eligibility

---

# Topic 5 – Functions

Functions allow reusable code.

Instead of writing the same code multiple times, create a function once and call it whenever needed.

### Syntax

```python
def function_name():
    pass
```

### Example

```python
def greet():
    print("Hello")
```

---

# Topic 6 – Functions with Parameters

Parameters allow functions to receive values.

### Example

```python
def greet(name):
    print("Hello", name)

greet("John")
```

---

# Topic 7 – Return Values

Functions can return data using `return`.

### Example

```python
def add(a, b):
    return a + b

print(add(10, 20))
```

---

# Topic 8 – Default Parameters

Default values allow optional arguments.

### Example

```python
def greet(name="Guest"):
    print("Welcome", name)
```

---

# Topic 9 – Variable Scope

Scope determines where variables can be used.

## Global Variable

Accessible everywhere.

```python
x = 100
```

## Local Variable

Accessible only inside function.

```python
def demo():
    y = 50
```

---

# Mini Projects Included

## Project 1 – Grade Calculator

Calculates student grade based on marks.

Concepts:

* if
* elif
* conditions

---

## Project 2 – Temperature Converter

Converts Celsius into Fahrenheit.

Formula:

F = (C × 9/5) + 32

---

## Project 3 – Login Validation

Checks username and password.

Concepts:

* conditions
* logical operators

---

## Project 4 – Factorial Calculator

Calculates factorial using functions.

Example:

5! = 120

---

# Folder Structure

```text
PYTHON_TASK2/
│
├── 01_positive_negative.py
├── 02_voting.py
├── 03_even_odd.py
├── 04_college_admission.py
├── 05_atm_validation.py
├── 06_employee_bonus.py
├── 07_grade.py
├── README.md
```

---

# Learning Outcomes

After completing this project:

* Understand decision making in Python
* Use if, else, elif
* Write nested conditions
* Work with logical operators
* Create reusable functions
* Understand return values
* Build simple projects

---
