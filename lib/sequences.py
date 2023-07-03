#!/usr/bin/env python3

def print_fibonacci(length):
    fibonacci = [0,1]
    if length == 0:
        print ([])
    elif length == 1:
        print ([0])
    elif length == 2:
        print ([0,1])
    else:
        index = 2
        while len(fibonacci) < 10:
            fibonacci.append(fibonacci[index - 1] + fibonacci[index - 2])
            index+=1
        print (fibonacci)
    pass

print_fibonacci(10)