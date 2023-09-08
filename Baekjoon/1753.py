import heapq
import sys
input = sys.stdin.readline


def dijkstra():
    q = []
    # 시작 노드 비용 0
    heapq.heappush(q, (0, start))
    distance[start] = 0
    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for node, value in graph[now]:
            cost = dist + value
            if cost < distance[node]:
                distance[node] = cost
                heapq.heappush(q, (cost, node))

v, e = map(int, input().split())
start = int(input())
graph = [[] for _ in range(v+1)]
INF = int(1e9)
distance = [INF for _ in range(v+1)]

for _ in range(e):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))

dijkstra()

for i in range(1, v+1):
    if distance[i] == INF:
        print("INF")
    else:
        print(distance[i])