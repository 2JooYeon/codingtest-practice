from collections import deque

n, m, k = map(int, input().split())
# 격자 포탑 데이터
graph = []
# 공격력이 0 이상인 포탑들의 좌표값을 key로하고, 공격력과 공격시키를 value로 갖는 dictionary
data = dict()
# 공격 횟수
attack_cnt = 0
for i in range(n):
    graph.append(list(map(int, input().split())))
    for j in range(m):
        if graph[i][j]:
            # (i, j)를 key로 [공격력, 공격시기]를 value로
            data[(i, j)] = [graph[i][j], 0]

# 공격자 위치
attacker = (0, 0)
# 공격 대상 위치
target = (0, 0)

# 우/하/좌/상
dx_4 = [0, 1, 0, -1]
dy_4 = [1, 0, -1, 0]

# 우/우하/하/좌하/좌/좌상/상/우상
dx_8 = [0, 1, 1, 1, 0, -1, -1, -1]
dy_8 = [1, 1, 0, -1, -1, -1, 0, 1]


# 공격자 찾는 함수
def find_attacker():
    global data, attacker
    attackers = sorted(data.items(), key=lambda x:(x[1][0], -x[1][1], -(x[0][0]+x[0][1]), -x[0][1]))
    attacker = attackers[0][0]


# 공격 대상 찾는 함수
def find_target():
    global data, target
    targets = sorted(data.items(), key=lambda x: (-x[1][0], x[1][1], (x[0][0] + x[0][1]), x[0][1]))
    target = targets[0][0]


# 레이저 공격이 가능하면 (ax, ay)에서 (tx, ty)로 가기 위한 최소 경로 반환
def layser_attack(ax, ay, tx, ty):
    visited = [[0 for _ in range(m)] for _ in range(n)]
    visited[ax][ay] = 1
    q = deque()
    q.append([[ax, ay]])
    path = []
    possible = False
    while q:
        # 현재 진행 중인 경로에서 위치 x, y
        path = q.popleft()
        x, y = path[-1]
        # 공격 대상에 도달했다면
        if x == tx and y == ty:
            possible = True
            break
        for i in range(4):
            # 행과 열이 연결되어 있으므로 나머지 연산 처리
            nx, ny = (x + dx_4[i]) % n, (y + dy_4[i]) % m
            if not visited[nx][ny] and graph[nx][ny] > 0:
                visited[nx][ny] = 1
                # path 원본을 변경하지 않고 새로운 리스트를 큐에 추가
                q.append(path + [[nx, ny]])

    # 레이저 공격이 가능한 경우
    if possible:
        visited = [[0 for _ in range(m)] for _ in range(n)]
        visited[tx][ty] = 1
        visited[ax][ay] = 1

        # 공격 대상에는 공격자의 공격력 만큼 피해를 입힌다.
        graph[tx][ty] -= graph[ax][ay]
        # data 변수 업데이트
        if graph[tx][ty] > 0:
            data[(tx, ty)][0] = graph[tx][ty]
        else:
            del data[(tx, ty)]

        # 레이저 경로에 있는 포탑은 공격자 공격력의 절반 만큼의 공격을 받는다.
        # 경로의 맨 처음과 끝은 공격자와 공격 대상이므로 제외
        for x, y in path[1:-1]:
            visited[x][y] = 1
            graph[x][y] -= (graph[ax][ay]//2)
            # data 변수 업데이트
            if graph[x][y] > 0:
                data[(x, y)][0] = graph[x][y]
            else:
                del data[(x, y)]
        return visited

    return None


# 포탄 공격 함수 (tx, ty)를 대상으로 공격하고 주변 8개의 방향에 있는 포탑까지 공격
def shot_attack(ax, ay, tx, ty):
    visited= [[0 for _ in range(m)] for _ in range(n)]
    visited[ax][ay]=1
    visited[tx][ty]=1
    # 공격 대상에는 공격자의 공격력 만큼 피해를 입힌다.
    graph[tx][ty] -= graph[ax][ay]
    # data 변수 업데이트
    if graph[tx][ty] > 0:
        data[(tx, ty)][0] = graph[tx][ty]
    else:
        del data[(tx, ty)]

    # 공격 대상 주변의 8개의 방향에 있는 포탑은 공격자 공격력의 절반 만큼의 공격을 받는다.
    for i in range(8):
        nx, ny = (tx+dx_8[i])%n, (ty+dy_8[i])%m
        # 공격자는 제외
        if not (nx==ax and ny==ay) and graph[nx][ny] > 0:
            graph[nx][ny] -= (graph[ax][ay]//2)
            visited[nx][ny] = 1
            # data 변수 업데이트
            if graph[nx][ny] > 0:
                data[(nx, ny)][0] = graph[nx][ny]
            else:
                del data[(nx, ny)]
    return visited


# 포탑 정비 함수, 공격과 무관했던 포탑 공격력 +1
def update_graph(visited):
    for xy in data:
        x, y = xy
        if visited[x][y] != 1:
            graph[x][y] += 1
            # data 변수 업데이트
            data[(x, y)][0] = graph[x][y]


while attack_cnt < k:
    attack_cnt += 1
    # 공격자 위치 설정
    find_attacker()
    # 공격 대상 위치 설정
    find_target()
    # 공격자 공격력 증가
    graph[attacker[0]][attacker[1]] += (n+m)
    # data 변수 업데이트
    data[attacker][0] += (n+m)
    data[attacker][1] = attack_cnt

    # 레이저 공격이 가능할 경우 방문 배열 반환
    visited = layser_attack(attacker[0], attacker[1], target[0], target[1])
    if not visited:
        visited = shot_attack(attacker[0], attacker[1], target[0], target[1])

    # 부서지지 않은 포탑이 1개가 된다면 즉시 중단
    if len(data) == 1:
        break

    update_graph(visited)

print(max(map(max, graph)))



'''초기에 실패한 코드 분석'''
# q에 경로를 저장하지 않고 일반 bfs와 같이 방문한 노드 좌표 저장
# visited 변수에 이동 거리를 저장해놓고, 공격 대상(tx, ty)으로 부터 공격자(ax, ay)를 찾는 경로를 역순으로 구하려고 시도함
# 이 코드가 불가능한 이유는 단순히 방문하면 횟수가 증가하기 때문에 실제로 공격 대상까지 경로가 없음에도 이후 경로를 구하는 과정에서 사용된다
# ex)(9, 2)에서 (7, 0)으로 가고자 할때 (9,0)에서 (7,0)으로 갈 수 없음에도 5라는 값이 저장됨
#      [[4, 3, 2, 3, 4, 5]
#       [5, 0, 0, 4, 5, 6]
#       [6, 7, 8, 0, 6, 7]
#       [7, 8, 9, 8, 7, 8]
#       [8, 9, 0, 9, 8, 9]
#       [9, 0, 9, 8, 9, 0]
#       [8, 0, 8, 7, 0, 0]
#       [7, 8, 0, 6, 5, 6]
#       [0, 0, 0, 0, 4, 5]
#       [5, 0, 1, 2, 3, 4]]

# def layser_attack(ax, ay, tx, ty):
#     visited = [[0 for _ in range(m)] for _ in range(n)]
#     visited[ax][ay] = 1
#     possible = 0
#     q = deque()
#     q.append([ax, ay])
#     while q:
#         x, y = q.popleft()
#         for i in range(4):
#             nx, ny = (x + dx_4[i]) % n, (y + dy_4[i]) % m
#             if not visited[nx][ny] and graph[nx][ny] != 0:
#                 visited[nx][ny] = visited[x][y]+1
#                 q.append([nx, ny])
#             # 공격 대상 위치에 도달하면
#             if nx == tx and ny == ty:
#                 possible = 1
#                 ''' 여기서 함부로 break 해도 되나..? '''
#                 break
#     # 레이저 공격이 가능한 경우
#     if possible:
#         path = [[0 for _ in range(m)] for _ in range(n)]
#         now = visited[tx][ty]
#         x, y = tx, ty
#         shortest_path = []
#         path[x][y] = 1
#         path[ax][ay] = 1
#         # 최단 경로 찾기
#         while now>2:
#             for i in range(3, -1, -1):
#                 nx, ny = (x + dx_4[i]) % n, (y + dy_4[i]) % m
#                 if visited[nx][ny] == (now - 1):
#                     now -= 1
#                     shortest_path.append([nx, ny])
#                     path[nx][ny] = 1
#                     x, y = nx, ny
#                     break
#         # shortest_path.reverse()
#         # return shortest_path
#
#         # 공격 대상에는 공격자의 공격력 만큼 피해를 입힌다.
#         graph[tx][ty] -= graph[ax][ay]
#         if graph[tx][ty] != 0:
#             data[(tx, ty)][0] = graph[tx][ty]
#         else:
#             del data[(tx, ty)]
#         # 레이저 경로에 있는 포탑은 공격자 공격력의 절반 만큼의 공격을 받는다.
#         for x, y in shortest_path:
#             graph[x][y] -= (graph[ax][ay]//2)
#             if graph[x][y] != 0:
#                 data[(x, y)][0] = graph[x][y]
#             else:
#                 del data[(x, y)]
#         return path
#     else:
#         return -1
