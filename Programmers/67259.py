'''
이 코드의 반례 (현재 코드는 (x, y)에 도착한 순간만 보고 값을 비교하기 때문에 틀렸음)
[[0,0,0,0,0,0,0,0,0,1],
[0,1,1,1,1,1,1,1,0,1],
[0,1,1,1,1,1,1,1,0,1],
[0,1,1,1,1,1,1,0,0,1],
[0,1,1,1,1,1,1,0,1,1],
[0,1,1,1,1,1,1,0,1,1],
[0,1,1,1,1,0,0,0,0,0],
[0,1,1,1,1,0,1,1,1,0],
[0,0,0,0,0,0,1,1,1,0],
[1,1,1,1,1,1,1,1,1,0]]
정답: 4200, 오답: 4500
'''
from collections import deque
def solution(board):
    INF = int(1e9)
    answer = INF
    # 상우하좌
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]
    q = deque()
    n = len(board)
    visited = [[INF] * n for _ in range(n)]
    visited[0][0] = 0
    visited[0][1] = 100
    visited[1][0] = 100
    q.append((0, 1, 100, 1))
    q.append((1, 0, 100, 0))

    while q:
        x, y, cost, d = q.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if nx < 0 or nx >= n or ny < 0 or ny >= n:
                continue
            nd = 0
            if i % 2:
                nd = 1
            if board[nx][ny] == 0:
                if d == nd:
                    if cost + 100 <= visited[nx][ny] + 500:
                        visited[nx][ny] = cost + 100
                        q.append((nx, ny, cost + 100, nd))
                else:
                    if cost + 600 <= visited[nx][ny] + 500:
                        visited[nx][ny] = cost + 600
                        q.append((nx, ny, cost + 600, nd))
    answer = visited[n - 1][n - 1]

    return answer
