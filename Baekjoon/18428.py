from itertools import combinations
from collections import deque

n = int(input())
# n*n 크기의 복도 데이터
school = []
# 선생님이 위치한 좌표 데이터
teacher = []
# 빈칸 좌표 데이터
blank = []
for i in range(n):
    school.append(input().split())
    for j in range(n):
        data = school[i][j]
        if data == 'T':
            teacher.append([i, j])
        if data == 'X':
            blank.append([i, j])

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


# direction 방향으로 학생을 감시하는 함수 (학생을 발견: True, 미발견: False)
def check_student(school, x, y, direction):
    q = deque([[x, y]])
    while q:
        x, y = q.popleft()
        # 주어진 방향만 확인
        nx, ny = x + dx[direction], y + dy[direction]
        if nx<0 or nx>=n or ny<0 or ny>=n:
            continue
        # 빈칸 또는 선생님을 만나면 큐에 넣고 계속 진행
        if school[nx][ny]=='X' or school[nx][ny]=='T':
            q.append([nx, ny])
        # 학생을 발견하면 True 반환
        if school[nx][ny] == 'S':
            return True
        # 학생을 발견하기 전에 장애물을 만나면 False 반환
        if school[nx][ny] == 'O':
            return False
    return False


# 장애물을 설치할 후보 좌표 3개
combi = combinations(blank, 3)
for obs in combi:
    # 빈칸에 장애물 설치
    for i, j in obs:
        school[i][j] = 'O'
    # 학생을 발견했는지 확인하는 flag 변수
    state = False
    for i, j in teacher:
        # 상하좌우 모든 방향에 대해서 확인
        for direction in range(4):
            # 만약 학생을 발견했다면 state는 True
            if check_student(school, i, j, direction):
                state = True
                break
    # 모든 선생님들이 상하좌우 방향으로 감시했는데도 학생이 발견되지 않은 경우
    if not state:
        print('YES')
        break
    # 감시 후 복도 상태 원상 복구
    for i, j in obs:
        school[i][j] = 'X'

# 어떠한 경우에도 학생을 발견한 경우
if state:
    print('NO')
