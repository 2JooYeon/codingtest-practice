import sys
input = sys.stdin.readline

n, m = map(int, input().split())
graph = []
INF = int(1e9)
dp = [[[INF]*3 for _ in range(m)] for _ in range(n)]
for i in range(n):
    graph.append(list(map(int, input().split())))

for i in range(m):
    for j in range(3):
        dp[0][i][j] = graph[0][i]


# 1번째 행부터 바로 위의 행에서 데이터를 가져오며 dp 테이블 갱신
for i in range(1, n):
    for j in range(m):
        # 위의 행에서 0번째 방향은 오른쪽 위, 1번째 방향은 바로 위, 2번째 방향은 왼쪽 위를 나타낸다.
        for d in range(3):
            if (j == 0 and d == 2) or (j == m - 1 and d == 0):
                continue
            if d == 0:
                dp[i][j][d] = graph[i][j] + min(dp[i-1][j+1][1], dp[i-1][j+1][2])
            elif d == 1:
                dp[i][j][d] = graph[i][j] + min(dp[i-1][j][0], dp[i-1][j][2])
            else:
                dp[i][j][d] = graph[i][j] + min(dp[i-1][j-1][0], dp[i-1][j-1][1])
                continue

print(min(sorted(dp[n-1], key=lambda x:min(x))[0]))