n, m = map(int, input().split())
graph = []
for i in range(n):
    graph.append(list(map(int, input().split())))

# balls[i]: i 번 칸에 들어있는 구슬 번호
balls = [0]*(n*n)
# xy_num[x][y]: x,y 위치의 칸의 번호
xy_num = [[0]*n for _ in range(n)]
bomb_num = [0, 0, 0, 0]

# 상/하/좌/우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def blizard_magic(d, s):
    # 상어의 위치
    x, y = n//2, n//2
    for i in range(s):
        x += dx[d]
        y += dy[d]
        if x<0 or x>=n or y<0 or y>=n:
            continue
        num = xy_num[x][y]
        balls[num] = 0

# 토네이도로 돌면서 balls, xy_num 초기화하기
def init():
    # 좌/하/우/상
    dx = [0, 1, 0, -1]
    dy = [-1, 0, 1, 0]
    # 출발점 정중앙
    x, y = n//2, n//2
    d = 0
    # 칸의 번호
    num = 1
    # 첫 번째 칸은 상어가 차지
    balls[0] = 0
    for i in range(1, n):
        unit = 2
        if i == n-1: unit = 3
        for _ in range(unit):
            for j in range(i):
                x += dx[d]
                y += dy[d]
                xy_num[x][y] = num
                balls[num] = graph[x][y]
                num += 1
            d = (d + 1) % 4

def move_balls():
    global balls
    new_balls = [0]*(n*n)
    new_num = 1
    for i in range(1, n*n):
        if balls[i] != 0:
            new_balls[new_num] = balls[i]
            new_num += 1
    balls = new_balls

def bomb_balls():
    is_bomb = False
    group = [1]
    head_ball_num = balls[1]
    for i in range(2, n*n):
        if head_ball_num == balls[i]:
            group.append(i)
        else:
            if len(group) >= 4:
                is_bomb = True
                for num in group:
                    balls[num] = 0
                    bomb_num[head_ball_num] += 1
            head_ball_num = balls[i]
            group = [i]
    return is_bomb

def reproduce_balls():
    global balls
    new_balls = [0]*(n*n)
    new_num = 1
    i = 1
    while True:
        if new_num > n*n-1 or balls[i] == 0: break
        if balls[i] != balls[i + 1]:
            new_balls[new_num] = 1
            new_balls[new_num + 1] = balls[i]
            new_num += 2
            i += 1
        elif balls[i] == balls[i+1]:
            if balls[i+1] == balls[i+2]:
                new_balls[new_num] = 3
                new_balls[new_num + 1] = balls[i]
                new_num += 2
                i += 3
            else:
                new_balls[new_num] = 2
                new_balls[new_num + 1] = balls[i]
                new_num += 2
                i += 2
    balls = new_balls


init()
for i in range(m):
    d, s = map(int, input().split())
    blizard_magic(d-1, s)
    move_balls()
    while bomb_balls():
        move_balls()
    reproduce_balls()
answer = 0

for i in range(1, 4):
    answer += i*bomb_num[i]
print(answer)
