# 방향키 모양 외의 4개의 테트로미노 처리하기
def dfs(x, y, cnt, temp_sum):
    global answer
    # 어느 경우에도 현재 dfs에서 answer값보다 큰 값이 나올 수 없을 때 종료
    if answer >= temp_sum + max_val * (4-cnt):
        return
    if cnt == 4:
        answer = max(temp_sum, answer)
        return

    for i in range(4):
        nx, ny = x+dx[i], y+dy[i]
        if nx<0 or nx>=n or ny<0 or ny>=m:
            continue
        if not visited[nx][ny]:
            visited[nx][ny] = 1
            dfs(nx, ny, cnt + 1, temp_sum+graph[nx][ny])
            visited[nx][ny] = 0


# 방향키 모양의 테트로미노 처리하기
def arrow_key(x, y):
    global answer
    i, j = 0, 0
    for i in range(4):
        temp_sum = graph[x][y]
        is_break = 0
        for j in range(4):
            if i == j:
                continue
            nx, ny = x+dx[j], y+dy[j]
            if nx<0 or nx>=n or ny<0 or ny>=m:
                is_break = 1
                break
            temp_sum += graph[nx][ny]
        if not is_break and j == 3:
            answer = max(answer, temp_sum)


n, m = map(int, input().split())
graph = []
answer = 0
for _ in range(n):
    graph.append(list(map(int, input().split())))
visited = [[0 for _ in range(m)] for _ in range(n)]
# graph에서 가장 큰 값
max_val = max(map(max, graph))

# 서, 동, 북, 남
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

for i in range(n):
    for j in range(m):
        visited[i][j] = 1
        dfs(i, j, 1, graph[i][j])
        visited[i][j] = 0
        arrow_key(i, j)

print(answer)
