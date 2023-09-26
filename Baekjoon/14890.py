def soltion(way):
    prev = way[0]
    now = 1
    cnt = 1
    while now < n:
        # 높이 크기 차이가 1보다 클 때
        if abs(way[now] - prev) > 1:
            return 0

        # 칸의 높이가 같을 때
        if way[now] == prev:
            cnt += 1
            now += 1

        # 한 칸이 높아졌을 때
        elif way[now] == prev + 1:
            # 경사로를 놓을 수 있는 경우
            if cnt >= l:
                cnt = 1
                prev = way[now]
                now += 1
            # 경사로를 놓을 수 없는 경우
            else:
                return 0

        # 한 칸이 낮아졌을 때
        elif way[now] == prev - 1:
            cnt = 1
            prev = way[now]
            now += 1
            flag = 1
            while now < n and cnt < l:
                if way[now] != prev:
                    flag = 0
                    break
                cnt += 1
                now += 1
            # 경사로를 놓을 수 없는 경우
            if flag == 0 or cnt < l:
                return 0
            # 경사로를 놓을 수 있는 경우
            else:
                cnt = 0

    return 1


answer = 0
n, l = map(int, input().split())
graph = []
for _ in range(n):
    row = list(map(int, input().split()))
    graph.append(row)
    # 행을 기준으로 지나갈 수 있는 길 확인
    answer += soltion(row)

for j in range(n):
    col = []
    for i in range(n):
        col.append(graph[i][j])
    # 열을 기준으로 지나갈 수 있는 길 확인
    answer += soltion(col)

print(answer)
