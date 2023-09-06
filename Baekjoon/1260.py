from collections import deque

def dfs(visited, start):
    visited[start] = 1
    print(start, end=' ')
    for node in graph[start]:
        if not visited[node]:
            visited[node] = 1
            dfs(visited, node)


def bfs(visited, start):
    q = deque([start])
    visited[start] = 1
    while q:
        now = q.popleft()
        print(now, end=' ')
        for node in graph[now]:
            if not visited[node]:
                visited[node] = 1
                q.append(node)


n, m, v = map(int, input().split())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

# 정점 번호가 작은 것을 먼저 방문하기 위해 정렬
for i in range(1, n+1):
    graph[i].sort()

visited = [0 for _ in range(n+1)]
dfs(visited, v)
print()
visited = [0 for _ in range(n+1)]
bfs(visited, v)