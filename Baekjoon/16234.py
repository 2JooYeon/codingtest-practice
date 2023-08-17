from collections import deque

n, l, r = map(int, input().split())
nation = []

for _ in range(n):
    nation.append(list(map(int, input().split())))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs(nation, visited, x, y):
    q = deque([[x, y]])
    visited[x][y] = 1
    # 연합 국가 좌표 데이터
    union = [[x, y]]
    # 연합의 인구수
    value = nation[x][y]
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx, ny = x+dx[i], y+dy[i]
            if nx<0 or nx>=n or ny<0 or ny>=n:
                continue
            if not visited[nx][ny] and l <= abs(nation[x][y] - nation[nx][ny]) <= r:
                q.append([nx, ny])
                visited[nx][ny] = 1
                union.append([nx, ny])
                value += nation[nx][ny]
    if len(union) == 1:
        return [], 0
    return union, value


answer = 0
while True:
    # 인구 이동 여부를 나타내는 flag 변수
    flag = 0
    visited = [[0 for _ in range(n)] for _ in range(n)]
    temp_union = []
    temp_value = []
    for i in range(n):
        for j in range(n):
            union, value = bfs(nation, visited, i, j)
            if len(union):
                temp_union.append(union)
                temp_value.append(value)
                flag = 1
    for i in range(len(temp_union)):
        for x, y in temp_union[i]:
            nation[x][y] = temp_value[i] // len(temp_union[i])
    answer += 1
    if flag == 0:
        answer -= 1
        break

print(answer)
