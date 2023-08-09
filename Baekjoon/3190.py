from collections import deque
n = int(input())
board = [[0 for _ in range(n)] for _ in range(n)]
k = int(input())
for _ in range(k):
    i, j = map(int, input().split())
    # 사과는 1로 표시
    board[i-1][j-1] = 1
l = int(input())
s_d = deque()
for _ in range(l):
    t, d = input().split()
    s_d.append([int(t), d])

# 동, 남, 서, 북
dxy = [(0, 1), (1, 0), (0, -1), (-1, 0)]
# 처음에 뱀이 오른쪽(동쪽)을 향하고 있기 때문에 인덱스 0
d = 0
# 시작할 떄 뱀은 맨 위, 맨 좌측에 위치
x, y = 0, 0
snake = deque()
time = 0


def is_wall(x, y):
    if x<0 or x>=n or y<0 or y>=n:
        return True
    else:
        return False


# 뱀이 벽과 부딪히거나 자기 자신의 몸과 부딪히면 게임 종료
while not is_wall(x, y) and board[x][y] != -1:
    snake.append([x, y])
    # 사과가 있다면
    if board[x][y] == 1:
        board[x][y] = -1
    # 그냥 빈칸이라면
    elif time > 0 and board[x][y] == 0:
        # 뱀이 있는 위치는 -1로 표시
        board[x][y] = -1
        # 꼬리 위치한 칸을 비워준다.
        i, j = snake.popleft()
        board[i][j] = 0

    if len(s_d) and time == s_d[0][0]:
        direction = s_d.popleft()[1]
        # 오른쪽으로 90도 회전(시계방향)
        if direction == 'D':
            d = (d+1) % 4
        # 왼쪽으로 90도 회전(반시계방향)
        else:
            d = (d-1) % 4

    dx, dy = dxy[d]
    x += dx
    y += dy
    time += 1

print(time)
