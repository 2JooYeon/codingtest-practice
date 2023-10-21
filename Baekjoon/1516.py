import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
graph = [[] for _ in range(n+1)]
indegree = [0] * (n+1)
cost = [0] * (n+1)

for i in range(1, n+1):
    data = list(map(int, input().split()))
    cost[i] = data[0]
    for node in data[1:-1]:
        graph[node].append(i)
        indegree[i] += 1

dp = [0] * (n+1)
q = deque()
for i in range(1, n+1):
    if indegree[i] == 0:
        q.append(i)

while q:
    now = q.popleft()
    dp[now] += cost[now]
    for node in graph[now]:
        indegree[node] -= 1
        dp[node] = max(dp[node], dp[now])
        if indegree[node] == 0:
            q.append(node)

for i in range(1, n+1):
    print(dp[i])