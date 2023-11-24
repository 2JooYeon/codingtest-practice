def solution(commands):
    answer = []
    # 병합 상태를 확인하는 그래프
    graph = [[(i, j) for j in range(51)] for i in range(51)]
    # 셀의 문자열 상태를 확인하는 그래프
    content = [['EMPTY'] * 51 for _ in range(51)]

    def update(command):
        if len(command) == 4:
            _, r, c, value = command
            r, c = int(r), int(c)
            x, y = graph[r][c]
            content[x][y] = value
        else:
            _, value1, value2 = command
            for i in range(1, 51):
                for j in range(1, 51):
                    if content[i][j] == value1:
                        content[i][j] = value2

    def merge(command):
        r1, c1, r2, c2 = map(int, command[1:])
        x1, y1 = graph[r1][c1]
        x2, y2 = graph[r2][c2]
        if content[x1][y1] == 'EMPTY':
            content[x1][y1] = content[x2][y2]
        for i in range(1, 51):
            for j in range(1, 51):
                if graph[i][j] == (x2, y2):
                    graph[i][j] = (x1, y1)

    def unmerge(command):
        r, c = map(int, command[1:])
        x, y = graph[r][c]
        value = content[x][y]
        for i in range(1, 51):
            for j in range(1, 51):
                if graph[i][j] == (x, y):
                    graph[i][j] = (i, j)
                    content[i][j] = 'EMPTY'
        content[r][c] = value

    for command in commands:
        command = command.split()
        if command[0] == 'UPDATE':
            update(command)
        elif command[0] == 'MERGE':
            merge(command)
        elif command[0] == 'UNMERGE':
            unmerge(command)
        else:
            r, c = map(int, command[1:])
            x, y = graph[r][c]
            answer.append(content[x][y])

    return answer
