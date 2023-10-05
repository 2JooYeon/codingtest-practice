# 토네이도가 한 칸 이동할 때 모래 흩날리기
def distribute_sand(x, y):
    # 격자 밖으로 나간 모래의 양
    sand_out = 0
    # 토네이도가 도착한 좌표의 기존 모래 양
    sand = graph[x][y]
    # 비율이 적혀있는 칸으로 이동한 모래의 양
    sand_stack = 0
    # 알파 비율만큼 모래가 더해질 좌표
    alpha_x, alpha_y = 0, 0
    # ratio상의 좌표가 graph 상의 좌표가 되기 위한 변화량
    dx, dy = x-2, y-2
    # i, j는 ratio 상의 좌표
    for i in range(5):
        for j in range(5):
            if ratio[i][j] == 0: continue
            # ni, nj는 graph 상의 좌표
            ni, nj = i + dx, j + dy
            # 알파 비율일 경우 마지막에 처리
            if ratio[i][j] == -1:
                alpha_x, alpha_y = ni, nj
                continue
            # 격자의 밖으로 나간 모래
            if ni<0 or ni>=n or nj<0 or nj>=n:
                sand_out += int(ratio[i][j]*sand)
            else:
                graph[ni][nj] += int(ratio[i][j]*sand)
            sand_stack += int(ratio[i][j]*sand)
    # 격자의 밖으로 나간 모래
    if alpha_x<0 or alpha_x>=n or alpha_y<0 or alpha_y>=n:
        sand_out += sand - sand_stack
    else:
        graph[alpha_x][alpha_y] += sand - sand_stack
    graph[x][y] = 0
    # 격자 밖으로 나간 모래 반환
    return sand_out


# 반시계 방향으로 한번 회전
def rotate():
    new_ratio = []
    for j in range(4, -1, -1):
        row = []
        for i in range(5):
            row.append(ratio[i][j])
        new_ratio.append(row)
    return new_ratio


# 알파 비율은 -1로 취급
ratio = [[0, 0, 0.02, 0, 0],
         [0, 0.1, 0.07, 0.01, 0],
         [0.05, -1, 0, 0, 0],
         [0, 0.1, 0.07, 0.01,0],
         [0, 0, 0.02, 0, 0]]

rotated_ratio = {}
rotated_ratio[0] = ratio
# 4개의 방향에 맞게 회전된 ratio 저장
for i in range(1, 4):
    ratio = rotate()
    rotated_ratio[i] = ratio

n = int(input())
graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))

# 서, 남, 동, 북 (반시계 방향)
dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]
d = -1
x, y = n//2, n//2

answer = 0
# flag = 0
# 1, 1, 2, 2, 3, 3, ~ n-1, n-1 이동
for i in range(1, n):
    for _ in range(2):
        d = (d + 1) % 4
        # 미리 만들어둔 ratio 사용
        ratio = rotated_ratio[d]
        # if flag == 0:
        #     flag = 1
        # else:
        #     ratio = rotate()
        #     flag = 1
        for _ in range(i):
            nx, ny = x+dx[d], y+dy[d]
            sand_out = distribute_sand(nx, ny)
            answer += sand_out
            x, y = nx, ny

# 마지막 n-1 이동
d = (d + 1) % 4
ratio = rotated_ratio[d]
for i in range(n-1):
    nx, ny = x + dx[d], y + dy[d]
    answer += distribute_sand(nx, ny)
    x, y = nx, ny

print(answer)
