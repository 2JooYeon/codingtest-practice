from collections import deque


def bfs(start):
    q = deque([start])
    visited[start] = 1
    while q:
        now = q.popleft()
        for node in graph[now]:
            if not visited[node]:
                parent[node] = now
                visited[node] = 1
                q.append(node)


n = int(input())
graph = [[] for _ in range(n+1)]
for _ in range(n-1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
parent = [0 for _ in range(n+1)]
visited = [0 for _ in range(n+1)]
bfs(1)
for i in range(2, n+1):
    print(parent[i])
