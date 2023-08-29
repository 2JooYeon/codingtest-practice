import copy

answer = 0
graph = []
for _ in range(4):
    data = list(map(int, input().split()))
    temp = []
    for i in range(0, 8, 2):
        # (물고기 번호, 방향)
        temp.append([data[i], data[i+1]-1])
    graph.append(temp)

# 방향 1번부터 8번 순서대로 정의
dx = [-1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, -1, -1, -1, 0, 1, 1, 1]


# 특정 번호의 물고기 위치 찾는 함수
def find_fish(graph, num):
    for i in range(4):
        for j in range(4):
            if graph[i][j][0] == num:
                return (i, j)
    return (-1, -1)


# 모든 물고기를 이동시키는 함수
def move_fish(graph, shark_x, shark_y):
    for num in range(1, 17):
        x, y = find_fish(graph, num)
        direction = graph[x][y][1]
        # 존재하지 않는 물고기라면 continue
        if x == -1: continue

        for i in range(8):
            nx, ny = x + dx[direction], y + dy[direction]
            # 경계를 넘지 않고, 상어가 있는 칸이 아니라면
            if 0<=nx<4 and 0<=ny<4 and (nx, ny) != (shark_x, shark_y):
                graph[x][y][1] = direction
                graph[x][y], graph[nx][ny] = graph[nx][ny], graph[x][y]
                break
            direction = (direction + 1) % 8


# 상어가 이동할 수 있는 위치 리스트 반환하는 함수
def get_next_position(graph, shark_x, shark_y):
    result = []
    direction = graph[shark_x][shark_y][1]
    for i in range(4):
        shark_x += dx[direction]
        shark_y += dy[direction]
        if 0<=shark_x<4 and 0<=shark_y<4:
            # 물고기가 있는 칸이라면
            if graph[shark_x][shark_y][0] != -1:
                result.append((shark_x, shark_y))
    return result


def dfs(graph, shark_x, shark_y, total):
    global answer
    graph = copy.deepcopy(graph)

    # 현재 위치 물고기 먹기
    total += graph[shark_x][shark_y][0]
    # 먹은 물고기 칸을 빈칸으로 업데이트
    graph[shark_x][shark_y][0] = -1

    # 물고기 이동
    move_fish(graph, shark_x, shark_y)

    # 상어가 이동 가능한 위치 찾기
    positions = get_next_position(graph, shark_x, shark_y)
    if len(positions) == 0:
        answer = max(answer, total)
        return
    # 이동할 수 있는 위치에 대해 수행
    for nx, ny in positions:
        dfs(graph, nx, ny, total)


dfs(graph, 0, 0, 0)
print(answer)