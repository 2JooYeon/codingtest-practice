import heapq
import sys
input = sys.stdin.readline

n = int(input())
m = int(input())
graph = [[] for _ in range(n+1)]
INF = int(1e9)
distance = [INF] * (n+1)
for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
start, end = map(int, input().split())

def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0

    while q:
        dist, now = heapq.heappop(q)
        if dist > distance[now]:
            continue
        for node, value in graph[now]:
            cost = dist + value
            if cost < distance[node]:
                distance[node] = cost
                heapq.heappush(q, (cost, node))

dijkstra(start)
print(distance[end])
