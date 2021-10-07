import time

def iterfibo(n):
    sum = 0
    for i in range(n+1):
        sum += i
    return sum

while True:
    nbr = int(input("Enter a number: "))
    if nbr == -1:
        break
    ts = time.time()
    fibonumber = iterfibo(nbr)
    ts = time.time() - ts
    print("Iterfibo(%d)=%d, time %.6f" %(nbr, fibonumber, ts))
