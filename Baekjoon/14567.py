from collections import deque
import sys
input = sys.stdin.readline
def topology_sort():
    result = []
    q = deque()
    for i in range(1, n+1):
        if indegree[i] == 0:
            q.append([i, 1])

    while q:
        now, semester = q.popleft()
        result.append([now, semester])
        for node in graph[now]:
            indegree[node] -= 1
            if indegree[node] == 0:
                q.append([node, semester+1])
    return result


n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]
indegree = [0 for _ in range(n+1)]
for _ in range(m):
    # a번 과목이 b번 과목의 선수 과목
    a, b = map(int, input().split())
    graph[a].append(b)
    indegree[b] += 1

result = topology_sort()
result.sort()
print(' '.join(map(str, [x[1] for x in result])))
