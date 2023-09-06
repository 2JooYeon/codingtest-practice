from collections import deque
from sys import stdin
input = stdin.readline


def bfs(start):
    count = 1
    q = deque([start])
    visited = [0 for _ in range(n + 1)]
    visited[start] = 1
    while q:
        now = q.popleft()
        for node in graph[now]:
            if not visited[node]:
                count += 1
                visited[node] = 1
                q.append(node)
    return count

n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, input().split())
    # b를 해킹하면, a도 해킹할 수 있으므로
    graph[b].append(a)
computer = []

for i in range(1, n+1):
    computer.append(bfs(i))

max_value = max(computer)
for i in range(len(computer)):
    if computer[i] == max_value:
        print(i+1, end=' ')
