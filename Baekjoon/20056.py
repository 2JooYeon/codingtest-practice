# 파이어볼 이동 함수
def move(graph, ball):
    x, y, m, s, d = ball
    nx, ny = x, y
    # 방향 d로 s칸 만큼 이동
    for i in range(s):
        nx = (nx+dx[d]) % n
        ny = (ny+dy[d]) % n
    graph[nx][ny].append([m, s, d])

# 이동이 모두 끝난 뒤 업데이트 함수
def merge_fireball(graph):
    new_fireball = []
    for i in range(n):
        for j in range(n):
            if len(graph[i][j]) == 1:
                m, s, d = graph[i][j][0]
                new_fireball.append([i, j, m, s, d])
            # 2개 이상의 파이어볼이 있는 경우
            elif len(graph[i][j]) > 1:
                total_m, total_s = 0, 0
                # 합쳐지는 파이어볼의 방향이 모두 홀수이거나 짝수인지 확인하는 변수
                odd, even = 1, 1
                for m, s, d in graph[i][j]:
                    total_m += m
                    total_s += s
                    if d%2:
                        even = 0
                    else:
                        odd = 0
                nm = total_m//5
                ns = total_s//len(graph[i][j])
                # 질량이 0인 파이어볼 소멸
                if nm == 0:
                    continue
                # 합쳐지는 파이어볼의 방향이 모두 홀수이거나 짝수인 경우
                if odd or even:
                    for l in range(4):
                        new_fireball.append([i, j, nm, ns, 2*l])
                else:
                    for l in range(4):
                        new_fireball.append([i, j, nm, ns, 2*l+1])

    return new_fireball


n, m, k = map(int, input().split())
fireball = []
for _ in range(m):
    # x, y, 질량, 속도, 방향
    x, y, m, s, d = map(int, input().split())
    fireball.append([x-1, y-1, m, s, d])

# 문제에 나온 숫자에 맞게 방향 설정
dx = [-1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, 1, 1, 1, 0, -1, -1, -1]

graph = []
for _ in range(k):
    graph = [[[] for _ in range(n)] for _ in range(n)]
    for ball in fireball:
        move(graph, ball)
    fireball = merge_fireball(graph)

print(sum([x[2] for x in fireball]))