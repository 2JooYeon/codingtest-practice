from collections import deque


# person_xy 위치에서 conv_xy 위치까지의 최단거리 경로를 반환하는 함수
def find_shortest_path(person_xy, conv_xy):
    visited = [[0 for _ in range(n)] for _ in range(n)]
    px, py = person_xy
    cx, cy = conv_xy
    visited[px][py] = 1
    q = deque()
    q.append([[px, py]])
    while q:
        path = q.popleft()
        x, y = path[-1]
        # 가고 싶은 편의점에 도착했다면 종료
        if x==cx and y==cy:
            return path
        for i in range(4):
            nx, ny = x+dx[i], y+dy[i]
            if nx<0 or nx>=n or ny<0 or ny>=n:
                continue
            # 아직 방문하지 않았고 막힌 칸이 아니라면 이동 가능
            if not visited[nx][ny] and not graph[nx][ny] == -1:
                visited[nx][ny] = 1
                q.append(path + [[nx, ny]])


# 행동 1: 격자에 있는 사람들 모두를 본인이 가고 싶은 편의점 방향을 향해 1칸 움직이는 함수
def move_to_conv_store():
    global people_xy
    new_people_xy = dict()
    for person_id in people_xy:
        # 현재 위치에서 가고 싶은 편의점까지의 최단 경로
        path = find_shortest_path(people_xy[person_id], people_conv_store[person_id])
        # 1 칸 이동
        new_people_xy[person_id] = path[1]
    # 사람들 위치 업데이트
    people_xy = new_people_xy


# 행동 2: 자신이 가고 싶은 편의점에 도착한 사람은 멈추게 하는 함수
def check_conv_store():
    global people_xy
    new_people_xy = dict()
    for person_id in people_xy:
        # 자신이 가고 싶어하는 편의점에 도착한 사람이 있는 경우
        if people_xy[person_id] == people_conv_store[person_id]:
            px, py = people_xy[person_id]
            # 해당 편의점을 지나갈 수 없도록 블락 처리
            graph[px][py] = -1
        else:
            new_people_xy[person_id] = people_xy[person_id]
    # 사람들 위치 업데이트
    people_xy = new_people_xy


# 자신이 가고 싶은 편의점과 가장 가까운 베이스 캠프의 위치를 찾는 함수
def find_nearest_basecamp(conv_xy):
    visited = [[0 for _ in range(n)] for _ in range(n)]
    cx, cy = conv_xy
    visited[cx][cy] = 1
    q = deque()
    q.append([cx, cy])
    while q:
        x, y = q.popleft()
        # 베이스 캠프에 도착했다면
        if graph[x][y] == 1:
            return [x, y]
        for i in range(4):
            nx, ny = x+dx[i], y+dy[i]
            if nx<0 or nx>=n or ny<0 or ny>=n:
                continue
            if not visited[nx][ny] and not graph[nx][ny] == -1:
                visited[nx][ny] = 1
                q.append([nx, ny])


# 행동 3: 자신이 가고 싶은 편의점과 가장 가까이 있는 베이스 캠프로 움직이는 함수
def move_to_basecamp(person_id):
    people_xy[person_id] = find_nearest_basecamp(people_conv_store[person_id])
    px, py = people_xy[person_id]
    graph[px][py] = -1


n, m = map(int, input().split())
graph = []
# 격자에 있는 사람들의 현재 위치를 저장하는 딕셔너리
people_xy = dict()
# 사람들의 선호 편의점 위치를 저장하는 딕셔너리
people_conv_store = dict()
for _ in range(n):
    # 0은 빈 공간, 1은 베이스캠프
    graph.append(list(map(int, input().split())))

for person_id in range(m):
    x, y = map(int, input().split())
    people_conv_store[person_id] = [x-1, y-1]

# 상/좌/우/하
dx = [-1, 0, 0, 1]
dy = [0, -1, 1, 0]
time = 0
while True:
    # 행동 1
    move_to_conv_store()
    # 행동 2
    check_conv_store()
    # 행동 3
    if time < m:
        move_to_basecamp(time)
    time += 1
    if len(people_xy)==0:
        break
print(time)
