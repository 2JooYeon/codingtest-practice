import heapq

n = int(input())
q = []
for _ in range(n):
    x = int(input())
    if x:
        heapq.heappush(q, (abs(x), x))
    else:
        if len(q):
            _, now = heapq.heappop(q)
            print(now)
        else:
            print(0)