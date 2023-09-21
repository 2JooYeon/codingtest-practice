from collections import deque

n, m = map(int, input().split())
board = []
# 빨간 구슬, 파란 구슬의 현재 위치를 나타낼 튜플
now_r = (0,0)
now_b = (0,0)
for i in range(n):
    board.append(list(input()))
    for j in range(m):
        if board[i][j] == 'R':
            now_r = (i, j)
        if board[i][j] == 'B':
            now_b = (i, j)

# 빨간 구슬 위치, 파란 구슬 위치
rb_pos = (now_r, now_b)
visited = [rb_pos]
q = deque()
# ((빨간 구슬 위치), (파란 구슬 위치)), 구슬을 굴린 횟수)
q.append((rb_pos, 0))
# 동 서 남 북 이동
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]


def solution():
    while q:
        rb_pos, count = q.popleft()
        # 10번 이하로 빨간 구슬을 뺼 수 없는 경우 실패
        if count >= 10:
            break
        (rx, ry), (bx, by) = rb_pos

        for i in range(4):
            # 각 구슬이 구멍에 빠졌는지 확인하는 변수
            r_hole = False
            b_hole = False
            # 각 구슬이 이동한 거리
            r_move = 0
            b_move = 0

            # 빨간 구슬 기울이기
            rnx, rny = rx, ry
            while board[rnx+dx[i]][rny+dy[i]] != '#':
                rnx += dx[i]
                rny += dy[i]
                r_move += 1
                # 빨간 공이 구멍을 통해 빠져나갔을 경우
                if board[rnx][rny] == 'O':
                    r_hole = True
                    break

            # 파란 구슬 기울이기
            bnx, bny = bx, by
            while board[bnx+dx[i]][bny+dy[i]] != '#':
                bnx += dx[i]
                bny += dy[i]
                b_move += 1
                # 파란 공이 구멍을 통해 빠져나갔을 경우
                if board[bnx][bny] == 'O':
                    b_hole = True
                    break

            # 파란 구슬이 빠진 경우 무시
            if b_hole:
                continue
            # 빨간 구슬만 빠진 경우 성공
            if r_hole:
                return count + 1

            # 빨간 구슬과 파란 구슬이 같은 칸에 있을 때
            if rnx == bnx and rny == bny:
                # 이동 수가 더 많은 구슬을 한칸 뒤로
                if r_move > b_move:
                    rnx -= dx[i]
                    rny -= dy[i]
                elif r_move < b_move:
                    bnx -= dx[i]
                    bny -= dy[i]

            next_rb_pos = ((rnx, rny), (bnx, bny))
            # 방문하지 않았던 위치 세트만 추가
            if next_rb_pos not in visited:
                q.append((next_rb_pos, count + 1))
                visited.append(next_rb_pos)

    return -1

print(solution())
