from collections import deque

# graph에서 각 팀의 좌표를 구하는 함수
def find_team():
    visited = [[0 for _ in range(n)] for _ in range(n)]
    team_id = -1
    for i in range(n):
        for j in range(n):
            # 아직 방문하지 않았고 머리사람을 찾는다면 팀 찾기 시작
            if not visited[i][j] and graph[i][j] == 1:
                team_id += 1
                visited[i][j] = 1
                team = []
                q = deque()
                q.append([i, j])
                while q:
                    x, y = q.popleft()
                    team.append([x, y])
                    for d in range(4):
                        nx, ny = x + dx[d], y + dy[d]
                        if nx<0 or nx>=n or ny<0 or ny>=n:
                            continue
                        # 머리(1) -> 2 -> 꼬리(3) 순서로 저장하기 위해
                        if not visited[nx][ny] and (0 < graph[nx][ny] < 4 and graph[nx][ny] <= graph[x][y]+1):
                            visited[nx][ny] = 1
                            q.append([nx, ny])
                team_xy[team_id] = team
    return team_xy


# 머리 사람 따라서 모든 팀을 한 칸 이동시키는 함수
def move_team():
    global team_xy
    new_team_xy = dict()
    for team_id in team_xy:
        # 머리사람과 꼬리사람이 붙어있는지 여부
        is_cir = 0
        # 머리사람 좌표
        hx, hy = team_xy[team_id][0]
        # 꼬리사람 좌표
        tx, ty = team_xy[team_id][-1]
        # 머리사람 한 칸 이동
        for i in range(4):
            nx, ny = hx + dx[i], hy + dy[i]
            if nx<0 or nx>=n or ny<0 or ny>=n:
                continue
            # 머리사람이 이동할 칸
            if 3 <= graph[nx][ny] <= 4:
                # 머리사람과 꼬리사람이 붙어있는 경우
                if graph[nx][ny] == 3:
                    is_cir = 1
                # 머리사람의 위치를 nx, ny로 설정
                hx, hy = nx, ny
                graph[hx][hy] = 1
                break
        # 머리사람을 따라 나머지 팀원들 모두 한 칸씩 이동
        for x, y in team_xy[team_id][:-2]:
            graph[x][y] = 2
        graph[team_xy[team_id][-2][0]][team_xy[team_id][-2][1]] = 3
        if not is_cir:
            graph[tx][ty] = 4
        # 팀 좌표 업데이트
        new_team_xy[team_id] = [[hx, hy]] + team_xy[team_id][:-1]
    team_xy = new_team_xy


# 현재 라운드에서 공이 출발할 위치와 던질 방향을 찾는 함수
def ball_check():
    d = (round//n)%4
    ball_line = round%n
    ball_xy = 0
    if d == 0:
        ball_xy = [ball_line, 0]
    elif d == 1:
        ball_xy = [n-1, ball_line]
    elif d == 2:
        ball_xy = [n-1-ball_line, n-1]
    elif d == 3:
        ball_xy = [0, n-1-ball_line]
    return ball_xy, d


# 공을 던지고 점수를 획득하는 함수
def throw_ball(ball_xy, d):
    global answer
    x, y = ball_xy
    # 주어진 방향대로 공을 한 칸씩 이동하며 사람 만나는지 확인
    for i in range(n):
        if i>0:
            x, y = x+dx[d], y+dy[d]
        # 사람을 만난 경우
        if graph[x][y] != 0 and graph[x][y] != 4:
            # 해당 팀에 점수 제공
            for team_id in team_xy:
                if [x, y] in team_xy[team_id]:
                    score = team_xy[team_id].index([x, y]) + 1
                    answer += (score ** 2)
                    # 해당 팀의 방향 바꾸기
                    reverse_team(team_id)
                    return


# 팀의 방향을 바꾸는 함수
def reverse_team(team_id):
    hx, hy = team_xy[team_id][0]
    tx, ty = team_xy[team_id][-1]
    graph[tx][ty] = 1
    graph[hx][hy] = 3
    team_xy[team_id].reverse()


# 격자 크기, 팀의 개수, 라운드 수
n, m, k = map(int, input().split())
graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))

# 우/상/좌/하 -> 라운드를 고려한 순서
dx = [0, -1, 0, 1]
dy = [1, 0, -1, 0]

# 각 팀의 좌표 {team_id:[[x1, x2],,,[xn, yn]]
team_xy = dict()
# 팀 별 좌표 구성하기
find_team()
round = 0
answer = 0
for _ in range(k):
    # 모든 팀 이동
    move_team()
    # 공 던질 준비
    ball_xy, d = ball_check()
    # 공 던지고 점수 획득
    throw_ball(ball_xy, d)
    round += 1
print(answer)
