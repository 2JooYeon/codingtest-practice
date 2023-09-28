# 빈칸 수를 세는 함수
def count_blank(board):
    cnt = 0
    for i in range(n):
        cnt += board[i].count(0)
    return cnt


# cctv를 회전시키는 함수
def rotate(direction, num):
    if num == 0:
        return direction
    rot_direction = []
    for d in direction:
        rot_direction.append((d+1)%4)
    return rot_direction


# 감시한 빈칸을 #로 처리하는 함수
def monitor(board, direction, x, y):
    for i in direction:
        nx, ny = x, y
        while True:
            nx += dx[i]
            ny += dy[i]
            if nx < 0 or nx >= n or ny < 0 or ny >= m or board[nx][ny] == 6:
                break
            if board[nx][ny] == 0:
                board[nx][ny] = '#'


def dfs(idx, board):
    global answer
    # 주어진 cctv개수 만큼 동작했다면 최솟값 반환
    if idx == len(cctv_xy):
        answer = min(answer, count_blank(board))
        return

    # 현재 다루는 cctv 번호, 위치 데이터
    cctv, x, y = cctv_xy[idx]
    # 깊은 복사
    direction = [x for x in cctv_rot_dir[cctv]]
    # 현재 cctv 번호에서 가능한 회전 수 만큼 반복
    for i in range(cctv_rot_num[cctv]):
        # 깊은 복사
        graph = [row[:] for row in board]
        # 회전
        direction = rotate(direction, i)
        # 감시 진행
        monitor(graph, direction, x, y)
        dfs(idx+1, graph)


n, m = map(int, input().split())
graph = []
# (cctv 번호, 행, 열) 데이터
cctv_xy = []
for i in range(n):
    # 0은 빈 칸, 6은 벽, 1~5는 cctv
    data = list(map(int, input().split()))
    graph.append(data)
    for j in range(m):
        if data[j] != 0 and data[j] != 6:
            # (cctv 번호, 행, 열) 저장
            cctv_xy.append((data[j], i, j))

# 동, 남, 서, 북
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
# cctv 번호별로 감시할 수 있는 방향 인덱스 설정
cctv_rot_dir = [0, [0], [0, 2], [0, 3], [0, 2, 3], [0, 1, 2, 3]]
# cctv 번호별로 회전할 수 있는 횟수(기존 방향 1회 기준)
cctv_rot_num = [0, 4, 2, 4, 4, 1]
answer = int(1e9)
dfs(0, graph)
print(answer)