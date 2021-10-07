import time

def iterfibo(n):
    if n == 0:
        return 0
    else:
        a = 0
        b = 1
        sum = 0

        for i in range(2, n+1):
            sum = a + b
            a = b
            b = sum
        return sum

while True:
    nbr = int(input("Enter a number: "))
    if nbr == -1:
        break
    ts = time.time()
    fibonumber = iterfibo(nbr)
    ts = time.time() - ts
    print("Iterfibo(%d)=%d, time %.6f" %(nbr, fibonumber, ts))
