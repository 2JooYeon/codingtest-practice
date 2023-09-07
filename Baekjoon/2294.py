n, k = map(int, input().split())
coins = []
for _ in range(n):
    coins.append(int(input()))

INF = int(1e9)
dp = [INF for _ in range(k+1)]
dp[0] = 0

for coin in coins:
    for i in range(coin, k+1):
        dp[i] = min(dp[i], dp[i-coin]+1)

if dp[k] == INF:
    print(-1)
else:
    print(dp[k])