import os

def suma(a, b):
    total = a + b

    return total


if __name__ == '__main__':
    TOKEN = os.getenv("TOKEN")
    print('Access to environment variable complete.')

    a = 7
    b = 3
    c = suma(a, b)
    print('Sum is: ' + str(c))
