import sys
from collections import deque
input = sys.stdin.readline


def bfs(mid):
    visited[start] = 1
    q = deque()
    q.append(start)
    while q:
        now = q.popleft()
        if now == end:
            return True
        for node, value in graph[now]:
            if not visited[node] and mid <= value:
                q.append(node)
                visited[node] = 1


n, m = map(int, input().split())

graph = [[] for _ in range(n+1)]
for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))

for i in range(1, n+1):
    graph[i].sort(reverse=True)


# 이분탐색을 이용해서 옮길 수 있는 물품들의 중량의 최댓값을 구하는 방식
start, end = map(int, input().split())
low, high = 1, int(1e9)
while low <= high:
    visited = [0 for _ in range(n+1)]
    mid = (low + high) // 2
    # mid 중량을 옮길 수 있다면 low를 +1
    if bfs(mid):
        low = mid+1
    # mid 중량을 옮길 수 없다면 high를 -1
    else:
        high = mid-1

print(high)