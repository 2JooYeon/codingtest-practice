t = int(input())
for _ in range(t):
    n = int(input())
    coins = list(map(int, input().split()))
    m = int(input())
    dp = [0 for _ in range(m+1)]
    dp[0] = 1
    # 동전이 오름차순으로 정렬되어 있으므로, 단위가 작은 동전 순서대로 테이블 갱신
    for coin in coins:
        for i in range(1, m+1):
            if i >= coin:
                dp[i] += dp[i-coin]
    print(dp[m])