import time

b = 7

def verdubbelB():
    dubbelB = b + b
    print(dubbelB)
verdubbelB()

huidigetijd = time
print(huidigetijd.strftime(("%H:%M:%S")))

def f(y):
    som = 2*y + 1
    return som

def g(x):
    som = 5 + x + 10
    return som

print(f(3)+g(3))
