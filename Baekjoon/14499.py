def up():
    dice[0][1], dice[1][1], dice[2][1], dice[3][1] = \
        dice[3][1], dice[0][1], dice[1][1], dice[2][1]


def down():
    dice[0][1], dice[1][1], dice[2][1], dice[3][1] = \
        dice[1][1], dice[2][1], dice[3][1], dice[0][1]


def right():
    dice[1][0], dice[1][1], dice[1][2], dice[3][1] = \
        dice[1][1], dice[1][2], dice[3][1], dice[1][0]


def left():
    dice[1][0], dice[1][1], dice[1][2], dice[3][1] = \
        dice[3][1], dice[1][0], dice[1][1], dice[1][2]


n, m, x, y, k = map(int, input().split())
graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))
orders = list(map(int, input().split()))
dice = [[0 for _ in range(3)] for _ in range(4)]

for order in orders:
    if order == 1:
        if y + 1 >= m: continue
        right()
        y += 1
    elif order == 2:
        if y - 1 < 0: continue
        left()
        y -= 1
    elif order == 3:
        if x - 1 < 0: continue
        up()
        x -= 1
    else:
        if x + 1 >= n: continue
        down()
        x += 1
    if graph[x][y] == 0:
        graph[x][y] = dice[3][1]
    else:
        dice[3][1] = graph[x][y]
        graph[x][y] = 0
    print(dice[1][1])




