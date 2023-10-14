n = int(input())
graph = [[0] * n for _ in range(n)]
student_fav = dict()
student_xy = dict()
for i in range(n * n):
    data = list(map(int, input().split()))
    student_fav[data[0]] = data[1:]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# 문제 조건에 맞춰 앉을 자리를 찾는 함수
def find_seat(student_id):
    fav_list = []
    for x in range(n):
        for y in range(n):
            temp_fav, temp_blank = 0, 0
            if graph[x][y] != 0:
                continue
            for i in range(4):
                nx, ny = x + dx[i], y + dy[i]
                if nx < 0 or nx >= n or ny < 0 or ny >= n:
                    continue
                if graph[nx][ny] in student_fav[student_id]:
                    temp_fav += 1
                if graph[nx][ny] == 0:
                    temp_blank += 1
            fav_list.append([temp_fav, temp_blank, x, y])
    '''문제 조건대로 우선순위를 고려해서 정렬'''
    fav_list.sort(key=lambda x:(-x[0], -x[1], x[2], x[3]))
    _, _, sx, sy = fav_list[0]
    return sx, sy


for student_id in student_fav:
    sx, sy = find_seat(student_id)
    student_xy[student_id] = sx, sy
    graph[sx][sy] = student_id

answer = 0
# 학생들 만족도 구하기
for student_id in student_xy:
    fav = 0
    x, y = student_xy[student_id]
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if nx < 0 or nx >= n or ny < 0 or ny >= n:
            continue
        if graph[nx][ny] in student_fav[student_id]:
            fav += 1
    if fav>0:
        answer += 10**(fav-1)

print(answer)