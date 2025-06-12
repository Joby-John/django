# functions are first class objects
# a function can have inner functions(functions defined inside it)
# a decorator is a function that takes another argumnet and enhances the behavior of 
# the passed function


def fun1():
    print("Inside function 1")

def fun2(f):
    print("Inside function 2")
    f()

def fun3():
    def fun4():
        print("fun4")
    fun4()

f = fun1
f()

print()
fun2(f)

fun3()


#decorators

def decFun(f):
    def innerFun():
        print("Welcome")
        f()
    return innerFun

def fun():
    print("User")

fun = decFun(fun)
fun()

# this can be shorthanded by @decFun

@decFun
def fun():
    print("User")
fun()

# so basically its written like 

def decorator(f):
    def wrapper():
        print("Hello")
        f()
    return wrapper

@decorator
def helloJoby():
    print("Joby")

@decorator
def helloJery():
    print("Jery")

helloJery()
helloJoby()

# parameterized decorator
import time
def repeater(n):
    def decorator(f):
        def wrapper():
            for i in range(n ,0 ,-1 ):
                print(i)
                time.sleep(1)
                
            f()
        return wrapper
    return decorator

@repeater(10)
def launch():
    print("launch")

launch()

            
