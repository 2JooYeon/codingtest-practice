from bisect import bisect_left, bisect_right

n, x = map(int, input().split())
data = list(map(int, input().split()))
data.sort()
left = bisect_right(data, x-1)
right = bisect_left(data, x+1)
if right-left == 0:
    print(-1)
else:
    print(right-left)

