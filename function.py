def greet():
    print("hello shruu")

greet()

# function with multiple lines

def student_info():
    print("Name: Shruti")
    print("Course: Computer Science")
    print("Year: 4th")

student_info()

# why functions are useful 
# instead of dumping everything into one giant program
# you can organize it 

def deposit():
    pass

def withdraw():
    pass

def check_balance():
    pass

def show_menu():
    pass

deposit()
withdraw()
check_balance()
show_menu()

# function with arguments
def greet(name):
    print("Hello" ,name)

greet("shruu")     #shruu is arguments

# function with a parameters

def greet(name):   #name is parameter
    print("hello", name)

greet("shruu")
greet("adiii")

# with multiple parameters

def introduce(name , age):
    print("Name:",name)
    print("Age:",age)

introduce("SHRUU" , 20)

# function for addition

def add():
    a = 10
    b = 20
    print(a + b)

add()

#But there's a problem.
# What if we want:
# 10 + 20
# 30 + 40
# 50 + 60
# We don't want three separate functions.

def add(a ,b):
    print(a + b)

add(10 , 20)
add(30 , 40)
add(50 , 60)

# return arguments
def add(a, b):
    return a + b

result = add(5 , 10)
print(result) 

# default arguments
def greet(Name = "shruu"):
    print("hello" ,Name)

greet()
greet("User")

# keyword arguments
def info(name ,age):
    print(name , age)

info(age = 20 , name = "shruu")

# variable length arguments
    # 1. *args(multiple values)

def add(*nums):
    total = 0
    for n in nums:
        total += n
    return total

print(add(1 , 2 , 3 , 4 , 5))

    # 2. **kwargs(key-value)

def display(**data):
    print(data)

display(name = "Shruu" , age = 20)

# scope
    # 1. local scope   (priority)

def test():
    x = 10
    print(x)

test()

    # 2. Global scope

x = 10

def show():
    print(x)

show()

# lambda function

square = lambda x: x*x
print(square(5))

# Recursion
def factorial(n):
    if( n == 0 or n == 1):
        return 1
    else:
        return n * factorial(n-1)

print(factorial(5))

def fibonacci(n):
    if (n == 0 or n == 1):
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

print(fibonacci(5))


