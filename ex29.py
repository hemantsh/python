# Exercise 29: Fibonacci Generator (Memory Efficiency)
# Practice Problem: Create a generator function that yields Fibonacci numbers up to N. Instead of returning a full list, it should yield values one by one.

# Exercise Purpose: If you need to generate a billion numbers, a list would crash your computer’s RAM. A Generator uses the yield keyword to return one value at a time and “pauses” its execution state. This is the key to handling Big Data in Python.

# Given Input: n = 8

def fib_gen(n) :
    a=0
    b=1
    curr = 0
    while curr < n:
        yield a
        a,b = b, a+b
        curr += 1
        
fib = fib_gen(7)
for num in fib :
    print(num, end= " " )
