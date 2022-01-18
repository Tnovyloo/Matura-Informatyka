def recur_fibonacci(n):
   if n <= 1:
       return n
   else:
       return recur_fibonacci(n - 1) + recur_fibonacci(n - 2)

def fib_itteration(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    p, w = 0, 1
    for i in range(n-1):
        p, w = w, p+w
    return w

nterms = 10

if nterms <= 0:
   print("Plese enter a positive integer")
else:
   print("Fibonacci sequence:")
   for i in range(nterms):
       print(recur_fibonacci(i))
