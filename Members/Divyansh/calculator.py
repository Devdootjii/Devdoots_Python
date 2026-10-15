# Day 7: Modules & imports
# Name: Divyansh
# What I learned today: apna module banana, use import karna, aur math/random library
# Where I got stuck & fixed it: import line comment thi aur ek hi function banaya tha; chaar alag functions kiye

def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return "Error: zero se divide nahi ho sakta!"

if __name__ == "__main__":
    print(add(2, 2))
    print(sub(100, 2))
    print(mul(6, 2))
    print(div(16, 8))
    print(div(2, 0))
