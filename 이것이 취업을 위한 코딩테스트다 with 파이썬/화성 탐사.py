import heapq


def dijkstra(graph, distance):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    q = []
    heapq.heappush(q, (graph[0][0], [0,0]))
    distance[0][0] = graph[0][0]
    while q:
        dist, now = heapq.heappop(q)
        x, y = now[0], now[1]
        if distance[x][y] < dist:
            continue
        for i in range(4):
            nx, ny = x+dx[i], y+dy[i]
            if 0<=nx<n and 0<=ny<n:
                cost = dist + graph[nx][ny]
                if cost < distance[nx][ny]:
                    distance[nx][ny] = cost
                    heapq.heappush(q, (cost, [nx, ny]))


answers = []
INF = int(1e9)
t = int(input())
for _ in range(t):
    n = int(input())
    graph = []
    for _ in range(n):
        graph.append(list(map(int, input().split())))
    distance = [[INF for _ in range(n+1)] for _ in range(n+1)]
    dijkstra(graph, distance)
    answers.append(distance[n-1][n-1])

for answer in answers:
    print(answer)