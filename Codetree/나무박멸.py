# 1. 나무 성장
def grow_tree():
    global graph
    new_graph = [[0 for _ in range(n)] for _ in range(n)]
    for x in range(n):
        for y in range(n):
            # 나무가 있는 칸 확인
            if graph[x][y] > 0:
                cnt = 0
                for d in range(4):
                    nx, ny = x+dx[d], y+dy[d]
                    if nx<0 or nx>=n or ny<0 or ny>=n:
                        continue
                    if graph[nx][ny]>0:
                        cnt += 1
                new_graph[x][y] = graph[x][y] + cnt
            # 벽, 제초제가 있는 칸은 기존 값 유지
            elif graph[x][y] < 0:
                new_graph[x][y] = graph[x][y]
    graph = new_graph

# 2. 나무 번식
def propogate_tree():
    global graph
    new_graph = [[0 for _ in range(n)] for _ in range(n)]
    for x in range(n):
        for y in range(n):
            # 나무가 있는 칸 확인
            if graph[x][y]>0:
                # 기존 값 유지
                new_graph[x][y] = graph[x][y]
                cnt = 0
                blank = []
                for d in range(4):
                    nx, ny = x+dx[d], y+dy[d]
                    if nx < 0 or nx >= n or ny < 0 or ny >= n:
                        continue
                    # 벽, 다른 나무, 제초제 모두 없는 칸 확인
                    if graph[nx][ny] == 0:
                        blank.append((nx, ny))
                        cnt += 1
                for nx, ny in blank:
                    # 이후 다른 나무로부터 번식이 또 진행될 수 있으므로 +로 처리
                    new_graph[nx][ny] += graph[x][y]//cnt
            # 벽, 제초제가 있는 칸은 기존 값 유지
            elif graph[x][y] < 0:
                new_graph[x][y] = graph[x][y]
    graph = new_graph


# 3. 제초제 뿌릴 경로와, 박멸되는 나무의 수 반환
def find_killer_xy():
    killed_tree = -1
    killer_path = []
    for x in range(n):
        for y in range(n):
            # 나무가 있는 칸 확인
            cnt = 0
            temp_path = []
            if graph[x][y]>0:
                temp_path.append((x, y))
                # x,y 에서 제초제를 뿌렸을 때 박멸되는 나무의 수
                cnt = graph[x][y]
                for d in range(4):
                    # 대각선 방향으로 k칸 만큼 확인
                    for i in range(1, k+1):
                        nx, ny = x+ddx[d]*i, y+ddy[d]*i
                        if nx < 0 or nx >= n or ny < 0 or ny >= n:
                            continue
                        # 나무가 있는 칸이면 전파 계속 진행
                        if graph[nx][ny] > 0:
                            temp_path.append((nx, ny))
                            cnt += graph[nx][ny]
                        # 빈칸 또는 제초제가 있는 칸까지만 전파하고 중단
                        if graph[nx][ny] < -1 or graph[nx][ny] == 0:
                            temp_path.append((nx, ny))
                            break
                        # 벽을 만나면 전파 중단
                        if graph[nx][ny] == -1:
                            break

            elif graph[x][y] == 0 or graph[x][y] < -1:
                    temp_path.append((x, y))

            if cnt > killed_tree:
                killed_tree = cnt
                killer_path = temp_path

    return killer_path, killed_tree

# 4. 나무 박멸
def spread_killer(path):
    for x, y in path:
        graph[x][y] = -c

# 5. 제초제 유지 기간 업데이트
def update_killer():
    for x in range(n):
        for y in range(n):
            # 살충제가 뿌려져 있는 칸 확인
            # 제초제 제거
            if graph[x][y] == -3:
                graph[x][y] = 0
            if graph[x][y] < -3:
                graph[x][y] += 1



# 격자 크기 n, 박멸 진행 수 m, 제초제 확산 범위 k, 제초제가 남아있는 년 수 c
n, m, k, c = map(int, input().split())
graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))
# 제초제를 -c로 설정할 계획이므로, 벽과 구분하기 위해 2만큼 차이를 둔다.
c = c+2
# 상/우/하/좌
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
# 좌상/우상/우하/좌하 대각선 방향
ddx = [-1, -1, 1, 1]
ddy = [-1, 1, 1, -1]

answer = 0
for year in range(m):
    grow_tree()
    propogate_tree()

    path, cnt = find_killer_xy()
    if cnt<=0:
        break
    update_killer()
    spread_killer(path)

    answer += cnt

print(answer)
