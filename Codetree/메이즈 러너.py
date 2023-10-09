# 모든 참가자 이동 함수
def move_participants():
    global participants, move_cnt
    # 출구 위치
    ox, oy = out[0], out[1]
    new_participants = []
    for px, py in participants:
        # 움직였는지 여부
        is_move = 0
        # 현재 위치에서 출구까지의 거리
        dist = abs(px-ox) + abs(py-oy)
        # 상/하/좌/우 순서로 이동
        for i in range(4):
            nx, ny = px+dx[i], py+dy[i]
            if nx<0 or nx>=n or ny<0 or ny>=n:
                continue
            # 빈 칸이라면 이동 가능
            if maze[nx][ny] == 0:
                # 이동 후 출구까지의 거리
                now = abs(nx-ox) + abs(ny-oy)
                # 이전보다 출구에 가까워진 경우
                if now < dist:
                    is_move = 1
                    move_cnt += 1
                    # 출구에 도달했다면 즉시 탈출하기 때문에 참가자 위치에서 제외
                    if not (nx==ox and ny==oy):
                        new_participants.append([nx, ny])
                    break
        if is_move==0:
            new_participants.append([px, py])
    # 참가자 위치 정보 업데이트
    participants = new_participants


# 한 명 이상의 참가자와 출구를 포함한 가장 작은 정사각형의 좌상단 위치와 정사각형 길이를 반환하는 함수
def find_square():
    ox, oy = out[0], out[1]
    # 2*2 크기부터 n*n 크기의 정사각형 확인
    for i in range(2, n + 1):
        # 좌상단부터 우하단까지 순서대로 정사각형 확인
        for j in range(i):
            for k in range(i):
                nx_start, nx_end = ox - i + 1 + j, ox + j
                ny_start, ny_end = oy - i + 1 + k, oy + k
                if nx_start < 0 or nx_end >= n or ny_start < 0 or ny_end >= n:
                    continue
                for px, py in participants:
                    if nx_start <= px <= nx_end and ny_start <= py <= ny_end:
                        cube_x, cube_y = nx_start, ny_start
                        cube_len = i
                        return (cube_x, cube_y, cube_len)


# 미로에서 정사각형 회전시키는 함수
def rotate_maze():
    global out, participants, maze
    new_participants = []
    ox, oy = out[0], out[1]
    # 부분 정사각형 좌상단의 위치와 정사각형 길이
    cube_x, cube_y, cube_len = find_square()

    # 회전한 미로를 저장할 변수
    rotated_maze = [row[:] for row in maze]
    for i in range(cube_len):
        for j in range(cube_len):
            rotated_maze[cube_x+i][cube_y+j] = maze[cube_x+cube_len-1-j][cube_y+i]
            # 회전된 벽은 내구도 -1
            if rotated_maze[cube_x+i][cube_y+j] > 0:
                rotated_maze[cube_x+i][cube_y+j] -= 1

    # 회전 후 참가자 위치 업데이트
    for px, py in participants:
        if cube_x<=px<cube_x+cube_len and cube_y<=py<cube_y+cube_len:
            nx, ny = cube_x+(py-cube_y), cube_y+cube_len-1-(px-cube_x)
            new_participants.append([nx, ny])
        else:
            new_participants.append([px, py])
    participants = new_participants
    maze = rotated_maze
    # 회전 후 출구 위치 업데이트
    out = cube_x+(oy-cube_y), cube_y+cube_len-1-(ox-cube_x)


n, m, k = map(int, input().split())
maze = []
participants = []
for _ in range(n):
    maze.append(list(map(int, input().split())))
for _ in range(m):
    x, y = map(int, input().split())
    participants.append([x-1, y-1])
x, y = map(int, input().split())
out = [x-1, y-1]
move_cnt = 0
# 상/하/좌/우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

for _ in range(k):
    # 모든 참가자 이동
    move_participants()
    # 모든 참가자가 탈출에 성공한다면, 게임 종료
    if len(participants)==0:
        break
    # 미로 회전
    rotate_maze()

print(move_cnt)
print(out[0]+1, end=' ')
print(out[1]+1)
