from collections import deque
n, m = map(int, input().split())
graph = []
for _ in range(n):
    graph.append(list(map(int, input())))

# visited[x][y][0]은 아직 벽을 안부순 상태, [x][y][1]은 부순 상태
visited = [[[0,0] for _ in range(m)] for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs():
    q = deque([])
    q.append([0, 0, 0])
    visited[0][0][0] = 1

    while q:
        x, y, z = q.popleft()
        if x == n-1 and y == m-1:
            return visited[x][y][z]
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if nx<0 or nx>=n or ny<0 or ny>=m:
                continue
            # 다음 칸이 벽인데, 이전에 벽을 부수지 않은 경우
            if graph[nx][ny] == 1 and z == 0:
                # 현재 이동거리 + 1 값 저장
                visited[nx][ny][1] = visited[x][y][0] + 1
                # 한번 벽을 부쉈으면 계속 부순 상태로 진행
                q.append([nx, ny, 1])
            # 다음 칸이 벽이 아니고, 이전에 방문한 적이 없다면
            if not visited[nx][ny][z] and graph[nx][ny] == 0:
                visited[nx][ny][z] = visited[x][y][z] + 1
                q.append([nx, ny, z])
    return -1

print(bfs())
