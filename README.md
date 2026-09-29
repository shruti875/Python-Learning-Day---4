# 🟢 Python Programming – Stage 5: Functions & Code Organization

## 📌 Overview

This stage focuses on **writing reusable, structured, and modular Python code** using functions. It helps transform basic programs into well-organized applications by reducing repetition and improving readability.

---

# 🎯 Goal

Learn how to:

* Create reusable code blocks
* Organize programs properly
* Pass data into functions
* Return results from functions
* Improve code structure and logic

---

# 🧠 1. Functions

A function is a reusable block of code.

```python id="f1"
def greet():
    print("Hello")
```

---

# 📥 2. Parameters

Variables defined inside function definition.

```python id="f2"
def greet(name):
    print("Hello", name)
```

---

# 📤 3. Arguments

Values passed to a function when calling it.

```python id="f3"
greet("Shruu")
```

---

# 🔁 4. Return Values

Used to send result back from function.

```python id="f4"
def add(a, b):
    return a + b
```

---

# ⚙️ 5. Default Arguments

Used when no value is passed.

```python id="f5"
def greet(name="User"):
    print("Hello", name)
```

---

# 🧾 6. Keyword Arguments

Pass values using parameter names.

```python id="f6"
def info(name, age):
    print(name, age)

info(age=20, name="Shruu")
```

---

# 🔄 7. Variable-Length Arguments

## *args → multiple values

```python id="f7"
def add(*nums):
    return sum(nums)
```

## **kwargs → key-value pairs

```python id="f8"
def show(**data):
    print(data)
```

---

# 🌍 8. Scope

Defines where variables are accessible.

* Local scope → inside function
* Global scope → outside function

---

# ⚡ 9. Lambda Functions

Short one-line anonymous functions.

```python id="f9"
square = lambda x: x * x
```

---

# 🔁 10. Recursion

A function that calls itself.

```python id="f10"
def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n-1)
```

---

# 🧪 Practice Work

Refactor previous projects using functions:

* Calculator
* Banking System
* Expense Tracker
* Employee Management System

👉 Break large code into small reusable functions.

---

# 🚀 Projects

## 🔬 Scientific Calculator

Functions for add, subtract, multiply, divide.

## 💸 Expense Management System

Add, view, and calculate expenses using functions.

## 👨‍💼 Employee Management System

Add and display employee records.

## 🏦 Banking Application

Deposit, withdraw, and check balance using modular functions.

---

# 🛠️ Key Benefits of Functions

* Code reusability
* Better organization
* Easier debugging
* Cleaner structure
* Scalable programs

---

# 📈 Final Outcome

After completing this stage, you will be able to:

* Write modular Python programs
* Break large problems into smaller functions
* Build structured real-world applications
* Understand core programming design principles

---

# ⭐ Final Note

Functions are the foundation of professional programming. If you master this stage, your code will stop being random scripts and start becoming real applications.

Practice is the only way this actually clicks 🚀
