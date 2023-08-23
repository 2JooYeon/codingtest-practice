import heapq
INF = int(1e9)

n, m, c = map(int, input().split())
graph = [[] for _ in range(n+1)]
distance = [INF] * (n+1)
for _ in range(m):
    x, y, z = map(int, input().split())
    graph[x].append((y, z))


def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0
    while q:
        dist, now = heapq.heappop(q)
        # 이전에 처리한 적이 있다면
        if distance[now] < dist:
            continue
        # 현재 노드(now)와 연결된 노드 확인
        for temp_node, temp_cost in graph[now]:
            cost = dist + temp_cost
            # 현재 노드를 거쳐서 다른 노드로 이동하는 거리가 더 짧다면
            if cost < distance[temp_node]:
                distance[temp_node] = cost
                heapq.heappush(q, (cost, temp_node))

dijkstra(c)
temp = [x for x in distance if x != INF]
num_city = len(temp) - 1
max_dist = max(temp)
print(num_city, max_dist)