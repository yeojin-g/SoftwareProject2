import time


def fibo_iter(n):
    num1, num2 = 0, 1
    for i in range(n-1):
        num1, num2 = num2, num1+num2
    return num1+num2

def fibo_rec(n):
    if n <= 1:
        return n
    return fibo_rec(n - 1) + fibo_rec(n - 2)
while True:
    nbr = int(input("Enter a number: "))
    if nbr == -1:
        break
    ts = time.time()
    fibonumber = fibo_rec(nbr)
    ts = time.time() - ts
    print("Fibo_rec(%d)=%d, time %.6f" %(nbr, fibonumber, ts))

    ts = time.time()
    fibonumber = fibo_iter(nbr)
    ts = time.time() - ts
    print("Fibo_iter(%d)=%d, time %.6f" % (nbr, fibonumber, ts))
