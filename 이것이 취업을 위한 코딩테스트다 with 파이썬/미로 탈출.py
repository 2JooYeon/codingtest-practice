from collections import deque

n, m = map(int, input().split())
maze = []
visited = [[0 for _ in range(m)] for _ in range(n)]
for _ in range(n):
    maze.append(list(map(int, list(input()))))

# 상하좌우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(graph, visited, x, y):
    q = deque([[x, y]])
    visited[x][y] = 1
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx, ny = x+dx[i], y+dy[i]
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            # 이전에 방문하지 않았고, 괴물이 없는 부분(1) 이라면
            if not visited[nx][ny] and graph[nx][ny]:
                visited[nx][ny] = 1
                q.append([nx, ny])
                graph[nx][ny] = graph[x][y] + 1

bfs(maze, visited, 0, 0)
print(maze[n-1][m-1])