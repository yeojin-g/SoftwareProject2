# 피보나치수열
import time

# 재귀함수
def recurfibo(n):
    if n < 2:
        return n
    else:
        return recurfibo(n-1) + recurfibo(n-2)
# 반복문
def iterfibo(n):
    if n < 2:
        return n
    else:
        a, b = 0, 1
        for i in range(n-1):
            a, b = b, a+b
        return b

while True:
    nbr = int(input("Enter a number :"))
    if nbr == -1:
        break
    start_time = time.time()
    fibonumber = iterfibo(nbr)
    end_time = time.time()
    itertime = end_time - start_time   #iterfibo에서 소요된 시간
    print("n={}, IterFibo={}, Itertime={}".format(nbr, fibonumber, itertime))

    start_time = time.time()
    fibonumber = recurfibo(nbr)
    end_time = time.time()
    recurtime = end_time - start_time   #recurfibo에서 소요된 시간
    print("n={}, RecurFibo={}, Recurtime={}".format(nbr, fibonumber, recurtime))