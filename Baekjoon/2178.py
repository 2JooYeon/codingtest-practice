from collections import deque

n, m = map(int, input().split())
maze = []
visited = [[0 for _ in range(m)] for _ in range(n)]
for _ in range(n):
    maze.append(list(map(int, input())))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs(graph, x, y):
    q = deque([[x, y]])
    visited[x][y] = 1

    while q:
        x, y = q.popleft()
        num = graph[x][y]
        for i in range(4):
            nx, ny = x+dx[i], y+dy[i]
            if nx<0 or nx>=n or ny<0 or ny>=m:
                continue
            if not visited[nx][ny] and graph[nx][ny] == 1:
                q.append([nx, ny])
                visited[nx][ny] = 1
                graph[nx][ny] = num + 1


bfs(maze, 0, 0)
print(maze[n-1][m-1])