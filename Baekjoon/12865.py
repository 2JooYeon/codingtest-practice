n, k = map(int, input().split())
things = [[0, 0]]
for _ in range(n):
    w, v = map(int, input().split())
    things.append([w, v])

# dp[n][k]는 n번째 물건까지 봤을 때, 무게가 k인 배낭의 최대 가치
dp = [[0 for _ in range(k+1)] for _ in range(n+1)]

# i: 현재 물건의 인덱스, j: 현재 가방의 무게 제한
# weight: 현재 담을 물건의 무게, value: 현재 담을 물건의 가치
for i in range(1, n+1):
    for j in range(1, k+1):
        weight, value = things[i]
        # 현재 허용 무게 보다 담을 물건의 무게가 클 때 -> 담지 않음
        if weight > j:
            dp[i][j] = dp[i-1][j]
        # 현재 물건을 무시하거나, 배낭에서 현재 물건 무게만큼 빼고 담거나
        else:
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-weight]+value)
print(dp[n][k])
