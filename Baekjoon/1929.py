import math
m, n = map(int, input().split())

arr = [True for _ in range(n+1)]
# 1은 소수가 아니므로 False
arr[1] = False
for i in range(2, int(math.sqrt(n))+1):
    if arr[i]:
        j = 2
        while i*j <= n:
            arr[i*j] = False
            j += 1

for i in range(m, n+1):
    if arr[i]:
        print(i)