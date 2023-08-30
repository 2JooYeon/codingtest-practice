from collections import defaultdict

n, m, k = map(int, input().split())
graph = []
# [상어 번호, 냄새가 남은 시간]을 저장하는 2차원 리스트
smell = [[[0, 0] for _ in range(n)] for _ in range(n)]
# {상어 번호: (상어 위치 x, 상어 위치 y)}를 기록하는 딕셔너리
shark_xy = {}
# {상어 번호: 상어의 방향}을 기록하는 딕셔너리
shark_direction = {}
# {상어 번호: {1: [방향 우선 순서], 2: [방향 우선 순서], 3: [방향 우선 순서], 4: [방향 우선 순서]}}을 기록하는 딕셔너리
shark_priority = defaultdict(dict)

for _ in range(n):
    graph.append(list(map(int, input().split())))

direction = list(map(int, input().split()))

# 상어 방향이랑 위치 초기화
for i in range(n):
    for j in range(n):
        num = graph[i][j]
        if num != 0:
            shark_direction[num] = direction[num-1]
            shark_xy[num] = [i, j]

# 각 상어의 방향 우선순위 초기화
for num in range(1, m+1):
    for i in range(4):
        shark_priority[num][i+1] = list(map(int, input().split()))

# 위, 아래, 왼쪽, 오른쪽 순서로 방향 정의 (인덱스 쉽게 접근하기 위해 0번째 값 추가)
dx = [0, -1, 1, 0, 0]
dy = [0, 0, 0, -1, 1]


# [상어 번호, 냄새 남은 시간]을 업데이트 하는 함수
def update_smell():
    for i in range(n):
        for j in range(n):
            # 빈칸이 아니라면 냄새 남은 시간 -1
            if smell[i][j][1] > 0:
                smell[i][j][1] -= 1
            # 상어가 있는 칸이라면 [상어 번호, 냄새 남은 시간 k] 초기화
            if graph[i][j] > 0:
                smell[i][j] = [graph[i][j], k]


# 모든 상어를 움직이는 함수
def move_sharks():
    # 이동한 결과를 담을 임시 2차원 리스트
    temp_graph = [[0 for _ in range(n)] for _ in range(n)]
    # 모든 상어에 대해
    for shark_num in shark_xy:
        # 현재 상어의 위치
        x, y = shark_xy[shark_num]
        # 이미 사라진 상어라면 건너뛰기
        if x == -1:
            continue
        # 현재 상어의 방향
        direction = shark_direction[shark_num]
        # 인접한 칸 중 아무 냄새가 없는 칸이 있으면 1, 없으면 0
        is_blank = 0
        # 현재 상어의 우선순위 방향에 따라 회전하며 냄새가 없는 칸이 있는지 확인
        for now_dir in shark_priority[shark_num][direction]:
            # 이동할 좌표
            nx, ny = x + dx[now_dir], y + dy[now_dir]
            # 경계를 벗어나지 않고
            if 0 <= nx < n and 0 <= ny < n:
                # 냄새가 없는 칸이라면 이동
                if smell[nx][ny][1] == 0:
                    # 방향 업데이트
                    shark_direction[shark_num] = now_dir
                    # 위치 업데이트
                    shark_xy[shark_num] = [nx, ny]
                    is_blank = 1

                    # 상어가 없는 칸이면
                    if temp_graph[nx][ny] == 0:
                        temp_graph[nx][ny] = shark_num
                    # 상어가 있으면 낮은 번호의 상어가 들어가야 함
                    else:
                        prev_shark_num = temp_graph[nx][ny]
                        min_shark_num = min(prev_shark_num, shark_num)
                        temp_graph[nx][ny] = min_shark_num
                        # 이전 상어 번호보다 현재 상어 번호가 더 작을때
                        if prev_shark_num != min_shark_num:
                            # 이전 상어는 쫓아내기
                            shark_xy[prev_shark_num] = [-1, -1]
                        # 현재 상어 번호보다 이전 상어 번호가 더 작을때
                        else:
                            # 현재 상어 쫓아내기
                            shark_xy[shark_num] = [-1, -1]
                    break

        # 상하좌우에 모두 냄새가 남아있다면, 자신의 냄새가 있는 칸으로 이동
        if is_blank == 0:
            for now_dir in shark_priority[shark_num][direction]:
                nx, ny = x + dx[now_dir], y + dy[now_dir]
                # 경계를 벗어나지 않고
                if 0 <= nx < n and 0 <= ny < n:
                    # 자신의 냄새가 있는 칸이라면
                    if smell[nx][ny][0] == shark_num:
                        # 방향 업데이트
                        shark_direction[shark_num] = now_dir
                        # 위치 업데이트
                        shark_xy[shark_num] = [nx, ny]
                        temp_graph[nx][ny] = shark_num
                        break
    return temp_graph


time = 0
# 1번 상어만 남을 때까지 반복
while True:
    update_smell()
    temp_graph = move_sharks()
    graph = temp_graph
    time += 1

    # 1번 상어만 남았는지 확인하는 변수
    only_one = 1
    for shark_num in range(2, m+1):
        if shark_xy[shark_num][0] != -1:
            only_one = 0

    if only_one:
        print(time)
        break

    if time >= 1000:
        print(-1)
        break
