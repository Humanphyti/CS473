fib = 0
usr = 24
a = 0
b = 0
total = 1
while fib < (usr + 1):
    if (total == 0):
        a += 1
    total = a + b
    a = b
    b = total
    fib += 1

print (total)
