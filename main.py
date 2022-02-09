import os
import time

def suma(a, b):
    total = a + b

    return total


if __name__ == '__main__':
    while True:
        time.sleep(1)
        TOKEN = os.getenv("TOKEN")
        print('Access to environment variable complete.')

        a = 7
        b = 3
        c = suma(a, b)
        print('Sum is: ' + str(c))
