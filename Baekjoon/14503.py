n, m = map(int, input().split())
r, c, d = map(int, input().split())
# 북, 동, 남, 서
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

graph = []
for _ in range(n):
    # 0은 빈칸, 1은 벽
    graph.append(list(map(int, input().split())))

graph[r][c] = 2
x, y = r, c
answer = 0
flag = 1
while True:
    # 현재 칸이 아직 청소되지 않은 경우, 현재 칸을 청소한다.
    if flag:
        graph[x][y] = 2
        answer += 1
        flag = 0
    for i in range(1, 5):
        # 반시계 방향 90도 회전
        temp_d = (d - i) % 4
        nx, ny = x + dx[temp_d], y + dy[temp_d]
        if nx < 0 or nx >= n or ny < 0 or ny >= m:
            continue
        # 청소되지 않은 빈칸이라면
        if graph[nx][ny] == 0:
            x, y = nx, ny
            d = temp_d
            flag = 1
            break
    # 현재 칸의 주변 4칸 중 청소되지 않은 빈 칸이 없는 경우
    if flag == 0:
        nx, ny = x - dx[d], y - dy[d]
        # 후진 한 칸이 범위를 벗어나거나 벽인 경우 작동 중단
        if nx < 0 or nx >= n or ny < 0 or ny >= m or graph[nx][ny] == 1:
            break
        x, y = nx, ny

print(answer)