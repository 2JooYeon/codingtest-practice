n, k = map(int, input().split())
coins = []
for _ in range(n):
    coins.append(int(input()))

dp = [0 for _ in range(k+1)]
# 0원을 만드는 경우의 수는 1
dp[0] = 1
for coin in coins:
    for i in range(1, k+1):
        if i >= coin:
            dp[i] += dp[i-coin]

print(dp[k])
