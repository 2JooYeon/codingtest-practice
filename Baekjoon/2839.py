n = int(input())
INF = int(1e9)
d = [INF for _ in range(n+1)]
d[0] = 0
for unit in [3,5]:
    for i in range(unit, n+1):
        if d[i-unit] != INF:
            d[i] = min(d[i], d[i-unit]+1)

if d[n] == INF:
    print(-1)
else:
    print(d[n])