from collections import deque
n = int(input())
graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))
group_xy = dict()
group_size = dict()
group_list = []
# 상/우/하/좌
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]


def make_group():
    global group_xy, group_size, group_list
    new_group_xy = dict()
    new_group_size = dict()
    new_group_list = []
    group_id = 0
    visited = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if not visited[i][j]:
                new_group_list.append(group_id)
                new_group_xy[group_id] = []
                new_group_size[group_id] = 0

                num = graph[i][j]
                visited[i][j] = 1
                q = deque()
                q.append([i, j])
                while q:
                    x, y = q.popleft()
                    new_group_xy[group_id].append((x, y))
                    new_group_size[group_id] += 1
                    for d in range(4):
                        nx, ny = x+dx[d], y+dy[d]
                        if nx<0 or nx>=n or ny<0 or ny>=n:
                            continue
                        if not visited[nx][ny] and graph[nx][ny] == num:
                            visited[nx][ny] = 1
                            q.append([nx, ny])
                group_id += 1
    group_xy = new_group_xy
    group_size = new_group_size
    group_list = new_group_list


# a, b 그룹간의 맞닿은 변 개수 구하는 함수
def get_common_length(a, b):
    common_length = 0
    visited = [[0 for _ in range(n)] for _ in range(n)]
    # 크기가 더 작은 그룹을 a로 잡기
    if group_size[b] < group_size[a]:
        a, b = b, a
    for ax, ay in group_xy[a]:
        if not visited[ax][ay]:
            visited[ax][ay] = 1
            q = deque()
            q.append([ax, ay])
            while q:
                x, y = q.popleft()
                for d in range(4):
                    nx, ny = x+dx[d], y+dy[d]
                    if nx<0 or nx>=n or ny<0 or ny>=n:
                        continue
                    if not visited[nx][ny] and (nx, ny) in group_xy[b]:
                        # 여기서는 연결된 다른 그룹의 좌표를 방문처리 하거나 큐에 넣으면 안된다.
                        # ex) 예제 그림처럼 G3과 G4의 공통 변의 길이를 구할 때 (2,3)을 3번 방문해야 하기 때문이다.
                        common_length += 1
    return common_length


# 그림 회전 함수
def rotate_art():
    global graph
    new_graph = [[0 for _ in range(n)] for _ in range(n)]
    # 십자 모양 반시계 방향 회전
    row, col = n//2, n//2
    for i in range(n):
        new_graph[row][i] = graph[i][col]
        new_graph[i][col] = graph[row][n-i-1]

    # 나머지 4개의 block 시계 방향 회전
    unit = (n-1)//2
    for i in range(unit):
        for j in range(unit):
            new_graph[i][j] = graph[unit-j-1][i]
            new_graph[i][j+unit+1] = graph[unit-j-1][i+unit+1]
            new_graph[i+unit+1][j] = graph[n-j-1][i]
            new_graph[i+unit+1][j+unit+1] = graph[n-j-1][i+unit+1]
    graph = new_graph


# 조화로움 값 계산
def get_score(a, b):
    ax, ay = group_xy[a][0]
    a_num = graph[ax][ay]
    bx, by = group_xy[b][0]
    b_num = graph[bx][by]
    common_length = get_common_length(a, b)
    return (group_size[a]+group_size[b]) * a_num * b_num * common_length


# 백트래킹으로 조합 구현
# arr에서 num개의 조합 구하기
def get_combination(num, result, cur):
    if len(result) == num:
        group_combi.append(result)
        return
    group_num = len(group_list)
    for i in range(cur, group_num):
        get_combination(num, result+[group_list[i]], i+1)

make_group()
answer = 0
for i in range(4):
    # 그룹 생성
    make_group()
    # 모든 조합에 대해 조화로움 값 계산
    group_combi = []
    get_combination(2, [], 0)
    for a, b in group_combi:
        score = get_score(a, b)
        if score > 0:
            answer += score
    if i < 3:
        rotate_art()
print(answer)
