from collections import deque


def topology_sort():
    result = []
    q = deque()

    for i in range(1, n+1):
        if indegree[i] == 0:
            q.append(i)
    while q:
        now = q.popleft()
        result.append(now)
        for node in graph[now]:
            indegree[node] -= 1
            if indegree[node] == 0:
                q.append(node)
    return result
n, m = map(int, input().split())
indegree = [0 for _ in range(n+1)]
graph = [[] for _ in range(n+1)]
for _ in range(m):
    # a가 b 앞에 서야함
    a, b = map(int, input().split())
    graph[a].append(b)
    indegree[b] += 1

result = topology_sort()
print(' '.join(map(str, result)))