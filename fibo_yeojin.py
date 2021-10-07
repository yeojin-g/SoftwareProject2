import time
def iterfibo(n): #피보나치 함수 반복문으로 구현
    num1 = 0
    num2 = 1
    if n <= 1:
        return n
    while 1 < n:
        answer = num1 + num2
        num1, num2 = num2, answer
        n -= 1
    return answer

def fibo(n): #피보나치 함수 재귀함수로 구현
    if n <= 1:
        return n
    return fibo(n - 1) + fibo(n - 2)

while True:
    nbr = int(input("Enter a number: "))
    if nbr == -1:
        break
    ts = time.time()
    fibonumber = iterfibo(nbr)
    ts = time.time() - ts
    print("IterFibo(%d)=%d, time %.6f" %(nbr, fibonumber, ts))
    fibonumber = fibo(nbr)
    ts = time.time() - ts
    print("Fibo(%d)=%d, time %.6f" % (nbr, fibonumber, ts))
