from collections import deque

INF = int(1e9)
n = int(input())
graph = []
shark_x, shark_y = 0, 0
for i in range(n):
    data = list(map(int, input().split()))
    graph.append(data)
    for j in range(n):
        # 아기 상어가 있는 위치
        if graph[i][j] == 9:
            shark_x, shark_y = i, j
            # 아기 상어의 시작 위치를 빈칸 처리
            graph[i][j] = 0


# 현재 물고기의 크기
shark_size = 2

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


# 아기상어로부터 최단 거리를 계산하는 함수
def bfs(graph, x, y):
    q = deque([[x, y]])
    distance = [[-1 for _ in range(n)] for _ in range(n)]
    distance[x][y] = 0
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx, ny = x+dx[i], y+dy[i]
            if nx<0 or nx>=n or ny<0 or ny>=n:
                continue
            # 아기 상어보다 크기가 작거나 같은 물고기는 지나갈 수 있음
            if distance[nx][ny] == -1 and graph[nx][ny] <= shark_size:
                q.append([nx, ny])
                distance[nx][ny] = distance[x][y] + 1

    return distance


# 먹을 물고기를 찾는 함수
def get_fish(distance):
    min_distance = INF
    x, y = 0, 0
    # 우선 순위가 위 -> 왼쪽 이므로 반복문 사용
    for i in range(n):
        for j in range(n):
            if distance[i][j] != -1 and 1 <= graph[i][j] < shark_size:
                if distance[i][j] < min_distance:
                    min_distance = distance[i][j]
                    x, y = i, j
    if min_distance == INF:
        return -1
    else:
        return x, y


# 몇 초 동안 물고기를 잡아 먹는지 체크
answer = 0
# 먹은 물고기 양 체크
num_fish = 0
while True:
    distance = bfs(graph, shark_x, shark_y)
    result = get_fish(distance)
    # 더이상 먹을 수 있는 물고기가 없을 때
    if result == -1:
        print(answer)
        break
    else:
        shark_x, shark_y = result
        answer += distance[shark_x][shark_y]
        # 물고기를 먹었을 경우 빈칸으로 처리
        graph[shark_x][shark_y] = 0
        num_fish += 1
        # 자신의 크기와 같은 수의 물고기를 먹으면 크기 1 증가
        if num_fish == shark_size:
            shark_size += 1
            num_fish = 0
