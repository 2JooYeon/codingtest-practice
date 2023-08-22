n, m = map(int, input().split())
coins = []
d = [99999] * (m+1)
for _ in range(n):
    coins.append(int(input()))

d[0] = 0
for i in range(n):
    for j in range(coins[i], m+1):
        if d[j-coins[i]] != 99999:
            d[j] = min(d[j], d[j-coins[i]]+1)

if d[m] == 99999:
    print(-1)
else:
    print(d[m])
