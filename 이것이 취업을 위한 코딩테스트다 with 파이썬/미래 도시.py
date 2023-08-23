INF = int(1e9)

n, m = map(int, input().split())
graph = [[INF for _ in range(n+1)] for _ in range(n+1)]

# 자기 자신에서 자기 자신으로 가는 비용 0으로 초기화
for a in range(1, n+1):
    for b in range(1, n+1):
        if a == b:
            graph[a][b] = 0

# 간선 비용 초기화
for _ in range(m):
    a, b = map(int, input().split())
    graph[a][b] = 1
    graph[b][a] = 1

x, k = map(int, input().split())

for t in range(1, n+1):
    for a in range(1, n+1):
        for b in range(1, n+1):
            graph[a][b] = min(graph[a][b], graph[a][t] + graph[t][b])

answer = graph[1][k] + graph[k][x]
if answer >= INF:
    print(-1)
else:
    print(answer)