from collections import deque

n = int(input())
indegree = [0] * (n+1)
time = [0] * (n+1)
d = [0] * (n+1)
graph = [[] for _ in range(n+1)]

for a in range(1, n+1):
    data = list(map(int, input().split()))
    time[a] = data[0]
    for node in data[1:-1]:
        graph[node].append(a)
        indegree[a] += 1


def topology_sort():
    q = deque()

    for i in range(1, n+1):
        if indegree[i] == 0:
            q.append(i)
            d[i] = time[i]

    while q:
        now = q.popleft()
        for i in graph[now]:
            indegree[i] -= 1
            d[i] = max(d[i], time[i] + d[now])
            if indegree[i] == 0:
                q.append(i)

topology_sort()
for t in d[1:]:
    print(t)