import os
import time

def clearTerminal():
    print('Clearing terminal in 2s')
    time.sleep(2)
    os.system('cls' if os.name == 'nt' else 'clear')

def variableLengthedArguments( *elements):
    """* symbol is used to pass variable lengthed arguments"""
    for x in elements:
        print(x)
    clearTerminal()
def keywordVaribleLengthArgumnets(type, **elements):
    """** is used when we want to pass named ones much like dictionary"""
    #here the type is mandatory and the elements are not, ie they can be empty

    #simple dictionary iteration
    print(type)
    for w,v in elements.items():
        print(f'{w}: {v}')

# def add_multiply(x, y):
#     """This is how we return multiple values, this returns as list"""
#     sum = x+y
#     product = x*y

#     return [sum, product]

def add_multiply(x, y):
    """This is how we return multiple values, this returns as tuple"""
    sum = x+y
    product = x*y

    return sum, product


if __name__ == '__main__':
    variableLengthedArguments(1, 2, 3)
    variableLengthedArguments(0, 2, 4)

    keywordVaribleLengthArgumnets('numbers', one = 1, two = 2, three = 3)
    keywordVaribleLengthArgumnets('pronunciation', L = 'el', O = 'ou', V = 'we', E = 'ie')

    sum, product = add_multiply(7, 5)
    print(f'sum: {sum}, product: {product}')