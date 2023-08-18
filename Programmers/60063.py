from collections import deque


def find_next_pos(board, pos, n):
    next_pos_list= []
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    rot_d = [-1, 1]
    pos = list(pos)
    x1, y1 = pos[0]
    x2, y2 = pos[1]

    # 상하좌우 평행이동
    for i in range(4):
        nx1, ny1 = x1 + dx[i], y1 + dy[i]
        nx2, ny2 = x2 + dx[i], y2 + dy[i]
        if nx1 < 0 or nx1 >= n or ny1 < 0 or ny1 >= n or \
                nx2 < 0 or nx2 >= n or ny2 < 0 or ny2 >= n:
            continue
        if board[nx1][ny1] == 0 and board[nx2][ny2] == 0:
            next_pos_list.append({(nx1, ny1), (nx2, ny2)})

    # 회전 case1: 로봇이 가로로 있을때
    if x1 == x2:
        for i in range(2):
            nx1, ny1 = x1 + rot_d[i], y1
            nx2, ny2 = x2 + rot_d[i], y2
            if nx1 >= 0 and nx1 < n and ny1 >= 0 and ny1 < n and \
                    nx2 >= 0 and nx2 < n and ny2 >= 0 and ny2 < n:
                if board[nx1][ny1] == 0 and board[nx2][ny2] == 0:
                    next_pos_list.append({(x1, y1), (nx1, y1)})
                    next_pos_list.append({(x2, y2), (nx2, y2)})

    # 회전 case2: 로봇이 세로로 있을때
    elif y1 == y2:
        for i in range(2):
            nx1, ny1 = x1, y1 + rot_d[i]
            nx2, ny2 = x2, y2 + rot_d[i]
            if nx1 >= 0 and nx1 < n and ny1 >= 0 and ny1 < n and \
                    nx2 >= 0 and nx2 < n and ny2 >= 0 and ny2 < n:
                if board[nx1][ny1] == 0 and board[nx2][ny2] == 0:
                    next_pos_list.append({(x1, y1), (x1, ny1)})
                    next_pos_list.append({(x2, y2), (x2, ny2)})
    return next_pos_list


def solution(board):
    n = len(board)
    pos = {(0, 0), (0, 1)}
    q = deque()
    q.append((pos, 0))
    visited = [pos]

    while q:
        pos, sec = q.popleft()
        if (n-1, n-1) in pos:
            return sec
        for next_pos in find_next_pos(board, pos, n):
            if next_pos not in visited:
                q.append((next_pos, sec+1))
                visited.append(next_pos)

    return 0