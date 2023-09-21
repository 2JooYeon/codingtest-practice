import copy

def move_block(graph, direction):
    # 오른쪽으로 이동 시킨 경우:
    if direction == 0:
        for i in range(n):
            # 가장 오른쪽 열부터 확인하기
            end = n-1
            for j in range(n-2, -1, -1):
                # 빈칸이 아니면
                if graph[i][j]:
                    # 값 임시저장 하고
                    data = graph[i][j]
                    # 빈칸으로 만들어주기
                    graph[i][j] = 0
                    if graph[i][end] == 0:
                        graph[i][end] = data
                    elif graph[i][end] == data:
                        graph[i][end] *= 2
                        end -= 1
                    else:
                        end -= 1
                        graph[i][end] = data

    # 왼쪽으로 이동 시킨 경우:
    if direction == 1:
        for i in range(n):
            # 가장 왼쪽 열부터 확인하기
            end = 0
            for j in range(1, n):
                # 빈칸이 아니면
                if graph[i][j]:
                    # 값 임시저장 하고
                    data = graph[i][j]
                    # 빈칸으로 만들어주기
                    graph[i][j] = 0
                    if graph[i][end] == 0:
                        graph[i][end] = data
                    elif graph[i][end] == data:
                        graph[i][end] *= 2
                        end += 1
                    else:
                        end += 1
                        graph[i][end] = data

    # 아래쪽으로 이동 시킨 경우:
    if direction == 2:
        for j in range(n):
            # 가장 아래쪽 행부터 확인하기
            end = n-1
            for i in range(n-2, -1, -1):
                # 빈칸이 아니면
                if graph[i][j]:
                    # 값 임시저장 하고
                    data = graph[i][j]
                    # 빈칸으로 만들어주기
                    graph[i][j] = 0
                    if graph[end][j] == 0:
                        graph[end][j] = data
                    elif graph[end][j] == data:
                        graph[end][j] *= 2
                        end -= 1
                    else:
                        end -= 1
                        graph[end][j] = data

    # 위쪽으로 이동 시킨 경우:
    if direction == 3:
        for j in range(n):
            # 가장 위쪽 행부터 확인하기
            end = 0
            for i in range(1, n):
                # 빈칸이 아니면
                if graph[i][j]:
                    # 값 임시저장 하고
                    data = graph[i][j]
                    # 빈칸으로 만들어주기
                    graph[i][j] = 0
                    if graph[end][j] == 0:
                        graph[end][j] = data
                    elif graph[end][j] == data:
                        graph[end][j] *= 2
                        end += 1
                    else:
                        end += 1
                        graph[end][j] = data

    return graph


def dfs(board, count):
    global answer
    if count == 5:
        for i in range(n):
            answer = max(answer, max(board[i]))
        return

    for i in range(4):
        graph = move_block(copy.deepcopy(board), i)
        dfs(graph, count + 1)


n = int(input())
board = []
for _ in range(n):
    board.append(list(map(int, input().split())))

answer = 0
dfs(board, 0)
print(answer)