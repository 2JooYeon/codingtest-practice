from collections import deque


def bfs():
    while tomato:
        x, y = tomato.popleft()
        for i in range(4):
            nx, ny = x+dx[i], y+dy[i]
            if nx<0 or nx>=n or ny<0 or ny>=m:
                continue
            if graph[nx][ny] == 0:
                graph[nx][ny] = graph[x][y] + 1
                tomato.append([nx, ny])


def check_tomato():
    answer = 0
    for i in range(n):
        if 0 in graph[i]:
            return -1
        else:
            answer = max(answer, max(graph[i]))
    return answer-1


m, n = map(int, input().split())
graph = []
tomato = deque()
for i in range(n):
    graph.append(list(map(int, input().split())))
    for j in range(m):
        if graph[i][j] == 1:
            tomato.append([i, j])

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

bfs()
print(check_tomato())

