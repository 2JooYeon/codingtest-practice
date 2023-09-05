from bisect import bisect_left

n = int(input())
arr = list(map(int, input().split()))
# 수열 뒤집기
arr = arr[::-1]
d = [arr[0]]

for i in range(1, n):
    # 새로 들어온 원소가 더 작은 경우
    if arr[i] > d[-1]:
        d.append(arr[i])
    # 새로 들어온 원소가 더 작은 경우
    elif arr[i] < d[-1]:
        left = bisect_left(d, arr[i])
        d[left] = arr[i]

print(len(d))
