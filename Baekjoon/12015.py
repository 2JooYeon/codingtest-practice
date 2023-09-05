from bisect import bisect_left

n = int(input())
arr = list(map(int, input().split()))

d = [arr[0]]
for i in range(1, n):
    # 새로 들어온 수가 클 때
    if arr[i] > d[-1]:
        d.append(arr[i])
    # 새로 들어온 수가 작을 때
    elif arr[i] < d[-1]:
        left = bisect_left(d, arr[i])
        d[left] = arr[i]

print(len(d))
