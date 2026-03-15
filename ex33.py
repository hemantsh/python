# Exercise 33: Memoization with lru_cache
# Practice Problem: Write a recursive function fibonacci(n) to calculate the nth number in the Fibonacci sequence. 
#     Use functools.lru_cache to optimize it so that it doesn’t recalculate the same values multiple times.

import functools

@functools.lru_cache
def fib_x(n) :
    if n == 0 or n == 1:
        return n
        
    return fib_x(n-1) + fib_x(n-2)

a = fib_x(6)
print(a)
