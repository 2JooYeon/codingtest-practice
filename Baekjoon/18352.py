from collections import deque
import sys
input = sys.stdin.readline

n, m, k, x = map(int, input().split())
graph = [[] for _ in range(n + 1)]
# 거리 -1로 초기화
distance = [-1 for _ in range(n + 1)]
# 출발점 거리 0으로 초기화
distance[x] = 0

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)


def bfs(graph, distance, x):
    q = deque([x])
    while q:
        now = q.popleft()
        for city in graph[now]:
            if distance[city] == -1:
                q.append(city)
                distance[city] = distance[now] + 1


bfs(graph, distance, x)
flag = 1
for i in range(1, n + 1):
    if distance[i] == k:
        flag = 0
        print(i)
if flag:
    print(-1)