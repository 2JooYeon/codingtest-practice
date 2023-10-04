# 모든 구름을 direction방향으로 distance만큼 이동
def move_cloud(direction, distance):
    new_clouds = []
    for x, y in clouds:
        nx = (x + dx[direction] * distance) % n
        ny = (y + dy[direction] * distance) % n
        # 구름에서 비가 내려 물의 양 1 증가
        graph[nx][ny] += 1
        new_clouds.append((nx, ny))
    return new_clouds


# 물복사버그 마법 시전
def copy_water_magic():
    for x, y in clouds:
        water_cnt = 0
        # 대각선 4 방향 확인
        for i in range(1, 8, 2):
            nx, ny = x + dx[i], y + dy[i]
            if nx<0 or nx>=n or ny<0 or ny>=n:
                continue
            # 물이 있는 바구니의 개수 확인
            if graph[nx][ny] > 0:
                water_cnt += 1
        graph[x][y] += water_cnt


def update_cloud_water(moved_clouds):
    new_clouds = []
    for i in range(n):
        for j in range(n):
            if (i, j) not in moved_clouds and graph[i][j] >= 2:
                graph[i][j] -= 2
                new_clouds.append((i, j))
    return new_clouds


n, m = map(int, input().split())
graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))

dx = [0, -1, -1, -1, 0, 1, 1, 1]
dy = [-1, -1, 0, 1, 1, 1, 0, -1]

clouds = [(n-1, 0), (n-1, 1), (n-2, 0), (n-2, 1)]
moves = []
for _ in range(m):
    d, s = map(int, input().split())
    moves.append((d, s))

for d, s in moves:
    clouds = move_cloud(d-1, s)
    copy_water_magic()
    clouds = update_cloud_water(clouds)

answer = 0
for i in range(n):
    for j in range(n):
        answer += graph[i][j]
print(answer)
