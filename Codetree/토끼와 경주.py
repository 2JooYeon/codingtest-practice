'''
<경주 진행> 단계에서 매 턴마다 점프한 토끼를 제외한 나머지 토끼들에게 x+y(이동한 위치) 점수를 부여하는데
이때, 나머지 토끼들을 순차적으로 돌며 점수를 부여하면 시간 초과가 발생한다.
따라서 점프한 토끼의 점수에서 x+y를 빼고, 뺀 만큼의 점수를 plus_score에 누적하여
<최고의 토끼 선정> 단계에서 가장 높은 점수를 가진 토끼에게 plus_score 점수를 더하여 출력한다.
'''
import heapq
# n*m 크기의 격자
n, m = 0, 0
# 명령의 수
q = int(input())
rabbit_distance = dict()
rabbit_score = dict()
rabbit_heap = []
plus_score = 0
# 상/하/좌/우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# 1. 경주 시작 준비
def ready_race(p, data):
    for i in range(0, p*2, 2):
        rid, rd = data[i:i+2]
        rabbit_distance[rid] = rd
        rabbit_score[rid] = 0
        # 점프 수, 행+열, 행, 열, 고유번호 순서로 저장 (처음에는 모두 0,0에 위치함)
        heapq.heappush(rabbit_heap, [0, 0, 0, 0, rid])

# 2. 경주 진행
def start_race(k, s):
    global plus_score
    selected_rabbit = []
    for _ in range(k):
        next_pos = []
        jump, xy, x, y, rid = heapq.heappop(rabbit_heap)
        jump += 1
        for i in range(4):
            rd = rabbit_distance[rid]
            nx, ny = x+(dx[i]*rd), y+(dy[i]*rd)
            if nx<0 or nx>=n: nx = fix_out_range(nx, n)
            if ny<0 or ny>=m: ny = fix_out_range(ny, m)
            '''heapq와 리스트 sort를 비교했을 때 미세하게 후자가 더 빨랐다.'''
            # heapq.heappush(next_pos, [-(nx+ny), -nx, -ny])
            next_pos.append([-(nx+ny), -nx, -ny])
        next_pos.sort()
        _, nx, ny = heapq.heappop(next_pos)
        nx *= -1
        ny *= -1
        # 토끼 이동
        heapq.heappush(rabbit_heap, [jump, nx+ny, nx, ny, rid])
        heapq.heappush(selected_rabbit, [-(nx+ny), -nx, -ny, -rid])
        '''시간초과 코드: get_score()함수를 통해 나머지 토끼에게 모두 접근하면 시간 초과 발생'''
        # get_score(rid, nx+ny+2)
        '''시간초과 해결: 현재 토끼의 점수에서 nx+ny+2 점수 빼기'''
        rabbit_score[rid] -= nx+ny+2
        plus_score += nx+ny+2
    _, _, _, rid = heapq.heappop(selected_rabbit)
    # k번 동안 한번이라도 뽑혔던 토끼 중 가장 우선순위가 높은 토끼에게 점수 s 부여
    rabbit_score[-rid] += s

def fix_out_range(num, limit):
    if num < 0: num *= -1
    if (num-1)//(limit-1) % 2 == 1:
        if num%(limit-1)==0: num = 0
        else: num = (limit-1)-(num%(limit-1))
    else:
        if num%(limit-1)==0: num = limit-1
        else: num = num % (limit - 1)
    return num

# rid를 제외한 나머지 토끼들 score만큼 점수 부여
# def get_score(ex_rid, score):
#     for rid in rabbit_score:
#         if rid != ex_rid:
#             rabbit_score[rid] += score


def change_distance(rid, L):
    rabbit_distance[rid] *= L


for _ in range(q):
    command = list(map(int, input().split()))
    t = command[0]
    # 경주 시작 준비
    if t == 100:
        n, m = command[1:3]
        ready_race(command[3], command[4:])
    if t == 200:
        k, s = command[1:3]
        start_race(k, s)
    if t == 300:
        rid, L = command[1:3]
        change_distance(rid, L)
    if t == 400:
        score = max(rabbit_score.values()) + plus_score
        print(score)
