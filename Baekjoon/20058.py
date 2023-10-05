from collections import deque

# 주어진 array를 시계 방향 90도 회전하는 함수
def rotate90(array):
    len_arr = len(array)
    rotated_arr = []
    for j in range(len_arr):
        temp = []
        for i in range(len_arr-1, -1, -1):
            temp.append(array[i][j])
        rotated_arr.append(temp)
    return rotated_arr


# 주어진 unit을 간격으로 unit*unit 크기의 부분배열을 시계방향 90도 회전하는 함수
def rotate_sub_array(unit):
    for i in range(0, n, unit):
        sub_row = graph[i:i+unit]
        for j in range(0, n, unit):
            sub_arr = [row[j:j+unit] for row in sub_row]
            rotated_sub_arr = rotate90(sub_arr)
            for k in range(unit):
                graph[i+k][j:j+unit] = rotated_sub_arr[k]
    return graph


# 얼음이 없는 칸의 좌표를 사전형으로 반환하는 함수
def find_blank():
    blank_xy = dict()
    for i in range(n):
        for j in range(n):
            if graph[i][j] == 0:
                blank_xy[(i, j)] = 1
    return blank_xy


# 얼음이 3개 이상과 인접해있지 않은 칸의 얼음 양 1 줄이는 함수
def decrease_ice(blank_xy):
    for i in range(n):
        for j in range(n):
            cnt = 0
            for k in range(4):
                nx, ny = i + dx[k], j + dy[k]
                if nx<0 or nx>=n or ny<0 or ny>=n:
                    cnt += 1
                elif (nx, ny) in blank_xy:
                    cnt += 1
                if cnt >= 2 and (i, j) not in blank_xy:
                    graph[i][j] -= 1
                    break


# (i, j) 좌표를 기준으로 얼음 덩어리 크기를 반환하는 함수
def find_big_ice(i, j, visited):
    q = deque()
    q.append([i, j])
    visited[i][j] = 1
    cnt = 1
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if nx<0 or nx>=n or ny<0 or ny>=n:
                continue
            if not visited[nx][ny] and graph[nx][ny]>0:
                q.append([nx, ny])
                visited[nx][ny] = 1
                cnt += 1
    return cnt


N, Q = map(int, input().split())
graph = []
# n*n 격자
n = 2**N
for _ in range(n):
    graph.append(list(map(int, input().split())))
step = list(map(int, input().split()))

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

for l in step:
    rotate_sub_array(2**l)
    # 얼음이 2개 이하로만 인접한 칸은 얼음의 양 1 감소
    blank_xy = find_blank()
    decrease_ice(blank_xy)

arr_sum = 0
big_ice = 0
visited = [[0 for _ in range(n)] for _ in range(n)]
for i in range(n):
    for j in range(n):
        elem = graph[i][j]
        arr_sum += elem
        if not visited[i][j] and elem > 0:
            big_ice = max(big_ice, find_big_ice(i, j, visited))

print(arr_sum)
print(big_ice)
