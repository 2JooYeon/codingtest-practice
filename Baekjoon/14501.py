n = int(input())
counsel = []
d = [0] * (n+1)
for _ in range(n):
    counsel.append(list(map(int, input().split())))
for x in range(n):
    if x + counsel[x][0] <= n:
        for i in range(x+counsel[x][0], n+1):
            d[i] = max(d[i], d[x] + counsel[x][1])
print(max(d))