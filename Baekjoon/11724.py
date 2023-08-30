from collections import deque
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]
visited = [0] * (n+1)
for _ in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)


def bfs(graph, start, visitied):
    q = deque([start])
    visitied[start] = 1

    while q:
        now = q.popleft()
        for node in graph[now]:
            if not visitied[node]:
                q.append(node)
                visitied[node] = 1

answer = 0
for i in range(1, n+1):
    if not visited[i]:
        bfs(graph, i, visited)
        answer += 1

print(answer)