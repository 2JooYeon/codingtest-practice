import heapq

INF = int(1e9)
n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]
distance = [INF for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)


def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0
    while q:
        dist, now = heapq.heappop(q)
        # 이미 처리한 적이 있다면 패스
        if dist > distance[now]:
            continue
        for node in graph[now]:
            cost = dist + 1
            if cost < distance[node]:
                distance[node] = cost
                heapq.heappush(q, (cost, node))


dijkstra(1)
max_distance = max(distance[1:])
print(distance.index(max_distance), max_distance, distance.count(max_distance))
