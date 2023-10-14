# 4*4 격자
n = 4
# 물고기들의 방향이 존재하는 그래프
graph = [[[] for _ in range(n)] for _ in range(n)]
# 물고기 마리 수, 연습 수
m, s = map(int, input().split())
for _ in range(m):
    x, y, d = map(int, input().split())
    graph[x-1][y-1].append(d-1)
# 상어의 위치
sx, sy = map(int, input().split())
sx, sy = sx-1, sy-1
# 냄새가 생긴 시간: (냄새 위치)
fish_smell = dict()

# 왼쪽부터 시계방향으로 45도 회전하는 인덱스
dx = [0, -1, -1, -1, 0, 1, 1, 1]
dy = [-1, -1, 0, 1, 1, 1, 0, -1]

# 물고기 복제 마법
def copy_fish(prev_grpah):
    for i in range(n):
        for j in range(n):
            for d in prev_grpah[i][j]:
                graph[i][j].append(d)
    return graph

# 모든 물고기 이동
def move_fish():
    global graph
    new_graph = [[[] for _ in range(n)] for _ in range(n)]
    for x in range(n):
        for y in range(n):
            for d in graph[x][y]:
                is_move = False
                for i in range(8):
                    is_smell = False
                    nd = (d-i)%8
                    nx, ny = x+dx[nd], y+dy[nd]
                    # 격자를 벗어나는 칸은 이동 불가
                    if nx<0 or nx>=n or ny<0 or ny>=n:
                        continue
                    # 상어가 있는 칸은 이동 불가
                    if nx == sx and ny == sy:
                        continue
                    # 물고기 냄새가 있는 칸은 이동 불가
                    for k in range(1, 3):
                        if step-k in fish_smell:
                            if (nx, ny) in fish_smell[step-k]:
                                is_smell = True
                                break
                    if is_smell: continue
                    # 이동할 수 있다면 새로운 그래프에 업데이트
                    new_graph[nx][ny].append(nd)
                    is_move = True
                    break

                # 이동할 수 없는 경우 그대로 남아있는다.
                if not is_move:
                    new_graph[x][y].append(d)
    graph = new_graph


# 상어가 연속해서 3칸 이동
def move_shark(cnt, path):
    global shark_path, fish_cnt, sx, sy, flag
    # 상/좌/우/하
    dx = [-1, 0, 1, 0]
    dy = [0, -1, 0, 1]
    if len(path) == 4:
        if cnt > fish_cnt:
            shark_path = path
            fish_cnt = cnt
        elif flag and cnt == 0 and fish_cnt == 0:
            shark_path = path
            fish_cnt = cnt
            flag = 0
        return

    for i in range(4):
        visited = False
        x, y = path[-1]
        nx, ny = x+dx[i], y+dy[i]
        if nx < 0 or nx >= n or ny < 0 or ny >= n:
            continue
        for a, b in path:
            if nx == a and ny == b and (a!=sx or b!=sy):
                visited = True
                move_shark(cnt, path+[[nx, ny]])
                break
        if not visited:
            move_shark(cnt + len(graph[nx][ny]), path+[[nx, ny]])


answer = 0
step = 0
for _ in range(s):
    origin_graph = [row2[:] for row2 in [row[:] for row in graph]]
    move_fish()
    shark_path, fish_cnt = [], 0
    flag = 1
    move_shark(0, [[sx, sy]])
    fish_smell[step]=[]
    for x, y in shark_path[1:]:
        if len(graph[x][y]):
            fish_smell[step].append((x, y))
            graph[x][y] = []
    sx, sy = shark_path[-1]
    if step-2 in fish_smell:
        del fish_smell[step-2]
    copy_fish(origin_graph)
    step += 1
for i in range(n):
    for j in range(n):
        answer += len(graph[i][j])
print(answer)