# i번 세로선 결과가 i번이 나오는지 확인하는 함수
def check():
    # 0번 세로선부터 n-1 세로선까지
    for i in range(n):
        # 현재 세로선의 위치
        col = i
        # 가로선을 순서대로 탐색
        for j in range(h):
            # 오른쪽 가로선이 1인 경우
            if graph[j][col]:
                col += 1
            # 왼쪽 가로선이 1인 경우
            elif col > 0 and graph[j][col-1]:
                col -= 1
        if i != col:
            return False
    return True


def dfs(cnt, x, y):
    global answer
    # 이미 최솟값이 아닌 경우 종료
    if cnt >= answer:
        return
    if check():
        answer = min(answer, cnt)
        return
    # 추가한 가로선 개수가 3개면 종료
    if cnt == 3:
        return

    # x번 가로선부터 h-1번 가로선까지
    for i in range(x, h):
        if i == x:
            col = y
        else:
            col = 0
        # col번 세로선부터 n-2번 세로선까지 돌면서 확인
        for j in range(col, n-1):
            # 오른쪽 가로선 2개가 연속으로 비어있으면
            if graph[i][j] == 0 and graph[i][j+1]==0:
                # 만약 왼쪽 가로선이 존재한다면 패스
                if j>0 and graph[i][j-1]: continue
                graph[i][j] = 1
                # 가로선이 연속으로 존재하면 안되기 때문에 j+2
                dfs(cnt + 1, i, j+2)
                graph[i][j] = 0


# 세로선, 가로선, 세로선마다 가로선을 놓을 수 있는 위치
n, m, h = map(int, input().split())
graph = [[0 for _ in range(n)] for _ in range(h)]
for _ in range(m):
    # b번 세로선과 b+1번 세로선을 a번 점선위치에 연결
    a, b = map(int, input().split())
    graph[a-1][b-1] = 1

answer = 4
dfs(0, 0, 0)
if answer > 3:
    print(-1)
else:
    print(answer)