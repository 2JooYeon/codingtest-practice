import heapq
import sys
input = sys.stdin.readline


INF = int(1e9)
n, e = map(int, input().split())
graph = [[] for _ in range(n+1)]
for _ in range(e):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))
v1, v2 = map(int, input().split())


def dijkstra(start):
    distance = [INF] * (n + 1)
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0

    while q:
        dist, now = heapq.heappop(q)
        if dist < distance[now]:
            continue
        for node, value in graph[now]:
            cost = dist + value
            if cost < distance[node]:
                distance[node] = cost
                heapq.heappush(q, (cost, node))
    return distance


'''(1->v1->v2->n) VS (1->v2->v1->n) 더 최단거리인걸로 선택'''

distance = dijkstra(1)
# 1번 노드에서 v1 노드까지 최단거리
dist_v1 = distance[v1]
# 1번 노드에서 v2 노드까지 최단거리
dist_v2 = distance[v2]

distance = dijkstra(v1)
# v1 노드에서 n 노드까지 최단거리
dist_v1_n = distance[n]
# v1 노드에서 v2 노드까지 최단거리
dist_v1_v2 = distance[v2]

distance = dijkstra(v2)
# v2 노드에서 n 노드까지 최단거리
dist_v2_n = distance[n]
# v2 노드에서 v1 노드까지 최단거리
dist_v2_v1 = distance[v1]

answer = min(dist_v1 + dist_v1_v2 + dist_v2_n, dist_v2 + dist_v2_v1 + dist_v1_n)
if answer >= INF:
    print(-1)
else:
    print(answer)
