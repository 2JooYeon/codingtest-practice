n, m = map(int, input().split())
x, y, now_dir = map(int, input().split())

# 북쪽, 동쪽, 남쪽, 서쪽
direction = [(-1, 0), (0, 1), (1, 0), (0, -1)]

# 전체 맵 정보
map_data = []

# 0: 육지, 1: 바다
for _ in range(n):
    map_data.append(list(map(int, input().split())))

answer = 1

while True:
    # 네 방향 모두 갈 수 없는 경우 flag는 1을 나타냄
    flag = 1
    # 가본 육지칸은 -1로 설정
    map_data[x][y] = -1
    for i in range(4):
        now_dir = (now_dir - 1) % 4
        dx, dy = direction[now_dir]
        nx, ny = x + dx, y + dy
        # 왼쪽 칸이 방문했던 칸인지 확인 하고, 방문 안했으면 왼쪽으로 한칸 전진
        if nx >= 0 and nx < n and ny >= 0 and ny < m and map_data[nx][ny] == 0:
            x, y = nx, ny
            answer += 1
            flag = 0
            break
    if flag:
        back_dir = (now_dir + 2) % 4
        dx, dy = direction[back_dir]
        nx, ny = x + dx, y + dy
        # 모든 방향이 이미 가본 칸이거나 바다라면, 현재 방향에서 한칸 뒤로 이동, 단 뒤쪽이 바다라면 프로그램 종료
        if nx < 0 or nx >= n or ny < 0 or ny >= m or map_data[nx][ny] == 1:
            print(answer)
            break
        x, y = nx, ny
