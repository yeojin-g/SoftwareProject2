import time
import random


def seqsearch(nbrs, target):
    for i in range(0, len(nbrs)):
        if (target == nbrs[i]):
            return i
    return -1

def recbinsearch(L, l, u, target):
    middle_idx = ((u-l) // 2) + l
    if(l == u-1):
        return -1
    if L[middle_idx] == target:
        return middle_idx
    elif L[middle_idx] < target:
        l = middle_idx + 1
    else:
        u = middle_idx

    return recbinsearch(L, l, u, target)


numofnbrs = int(input("Enter a number: "))
numbers = []

for i in range(numofnbrs):
    numbers += [random.randint(0, 999999)]

numbers = sorted(numbers)

numoftargets = int(input("Enter the number of targets: "))
targets = []
for i in range(numoftargets):
    targets += [random.randint(0, 999999)]

ts = time.time()
# binary search - recursive
cnt = 0
idx = 0
for target in targets:
    idx = recbinsearch(numbers, 0, len(numbers), target)
    if idx == -1:
        cnt += 1
ts = time.time() - ts
print("recbinsearch %d: not found %d time %.6f" % (numoftargets, cnt, ts))
print(idx)

ts = time.time()
# sequential search
cnt = 0
for target in targets:
    idx = seqsearch(numbers, target)
    if idx == -1:
        cnt += 1
ts = time.time() - ts
print("seqsearch %d: not found %d time %.6f" % (numoftargets, cnt, ts))
