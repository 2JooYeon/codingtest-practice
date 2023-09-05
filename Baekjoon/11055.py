import copy
n = int(input())
arr = list(map(int, input().split()))
d = arr.copy()

for i in range(n):
    for j in range(i):
        if arr[j] < arr[i]:
            d[i] = max(d[i], d[j] + arr[i])

print(max(d))
