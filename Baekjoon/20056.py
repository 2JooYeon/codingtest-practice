from collections import defaultdict


# 파이어볼 이동 함수
def move_fireball():
    global fireball
    new_fireball = defaultdict(list)
    for x, y in fireball:
        for m, s, d in fireball[(x, y)]:
            # 방향 d로 s칸 만큼 이동
            nx = (x+dx[d]*s) % n
            ny = (y+dy[d]*s) % n
            new_fireball[(nx, ny)].append((m, s, d))

    return new_fireball


# 이동이 모두 끝난 뒤 업데이트 함수
def merge_fireball():
    global fireball
    new_fireball = defaultdict(list)
    for x, y in fireball:
        # 파이어볼이 1개인 경우
        if len(fireball[(x, y)]) == 1:
            new_fireball[(x, y)] = fireball[(x, y)]
        # 파이어볼이 2개 이상인 경우
        elif len(fireball[(x, y)]) > 1:
            total_m, total_s = 0, 0
            # 합쳐지는 파이어볼의 방향이 모두 홀수이거나 짝수인지 확인
            odd, even = 1, 1
            for m, s, d in fireball[(x, y)]:
                total_m += m
                total_s += s
                if d%2:
                    even = 0
                else:
                    odd = 0
            nm = total_m//5
            ns = total_s//len(fireball[(x, y)])
            # 질량이 0인 파이어볼 소멸
            if nm == 0:
                continue
            # 합쳐지는 파이어볼의 방향이 모두 홀수이거나 짝수인 경우
            if odd or even:
                for l in range(4):
                    new_fireball[(x, y)].append((nm, ns, 2*l))
            else:
                for l in range(4):
                    new_fireball[(x, y)].append((nm, ns, 2 * l + 1))

    return new_fireball


n, m, k = map(int, input().split())
# 파이어볼 위치마다 (m, s, d) 저장하는 딕셔너리
fireball = defaultdict(list)
for _ in range(m):
    # x, y, 질량, 속도, 방향
    x, y, m, s, d = map(int, input().split())
    fireball[(x-1, y-1)].append((m, s, d))

# 문제에 나온 숫자에 맞게 방향 설정
dx = [-1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, 1, 1, 1, 0, -1, -1, -1]

for _ in range(k):
    fireball = move_fireball()
    fireball = merge_fireball()

answer = 0
for x, y in fireball:
    answer += sum([x[0] for x in fireball[(x, y)]])
print(answer)