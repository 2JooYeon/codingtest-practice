def dfs(visited, start):
    global answer
    visited[start] = 1
    for node in graph[start]:
        if not visited[node]:
            answer += 1
            visited[start] = 1
            dfs(visited, node)

n = int(input())
graph = [[] for _ in range(n+1)]
m = int(input())
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
answer = 0
visited = [0 for _ in range(n+1)]
dfs(visited, 1)
print(answer)