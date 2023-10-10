# 두 플레이어가 싸우는 함수
def fight(player1, player2):
    player1_score = player_skill[player1] + player_gun[player1]
    player2_score = player_skill[player2] + player_gun[player2]
    # (1) 초기 능력치 + 가지고 있는 총의 공격력의 합을 비교
    if player1_score > player2_score:
        winner, loser = player1, player2
    elif player1_score < player2_score:
        winner, loser = player2, player1
    # (1)의 값이 같은 경우
    else:
        # (2) 초기 능력치 비교
        if player_skill[player1]>player_skill[player2]:
            winner, loser = player1, player2
        else:
            winner, loser = player2, player1
    '''2-2-1'''
    # 이긴 플레이어는 score값의 차이 만큼 포인트 획득
    point[winner] += abs(player1_score-player2_score)
    '''2-2-2'''
    check_loser(loser)
    '''2-2-3'''
    # 이긴 플레이어는 가장 공격력이 높은 총을 획득한다.
    get_strongest_gun(winner)


def check_loser(player_id):
    x, y, d = player_xyd[player_id]
    # 가지고 있는 총을 해당 격자에 내려놓는다.
    if player_gun[player_id]:
        graph[x][y].append(player_gun[player_id])
    player_gun[player_id] = 0

    # 이동하려는 칸에 다른 플레이어가 있거나 격자 범위 밖인 경우, 빈 칸 보일때까지 시계방향 90도 회전
    for i in range(4):
        nd = (d+i)%4
        nx, ny = x + dx[nd], y + dy[nd]
        if nx<0 or nx>=n or ny<0 or ny>=n:
            continue
        # 이동한 칸의 빈칸 여부
        is_blank = True
        for j in range(m):
            if j != player_id:
                # 해당 칸에 다른 플레이어가 있다면
                if player_xyd[j][:2] == [nx, ny]:
                    is_blank = False
                    break
        if not is_blank:
            continue
        # 플레이어 위치 업데이트
        player_xyd[player_id] = [nx, ny, nd]
        # 가장 공격력이 높은 총을 획득한다.
        get_strongest_gun(player_id)
        return


# 가장 공격력이 높은 총을 획득하고 나머지 총을 칸에 내려 놓는 함수
def get_strongest_gun(player_id):
    x, y, d = player_xyd[player_id]
    # 해당 칸에 총이 없으면 아무 일도 일어나지 않는다.
    if not graph[x][y]:
        return
    # 플레이어가 이미 총을 가지고 있는 경우
    if player_gun[player_id]:
        # 갖고 있던 총을 칸에 내려 놓는다.
        graph[x][y].append(player_gun[player_id])
    # 현재 칸에서 가장 쎈 총 획득
    player_gun[player_id] = max(graph[x][y])
    # 획득한 총은 칸에서 삭제
    graph[x][y].remove(player_gun[player_id])


# 격자 크기, 플레이어 수, 라운드 수
n, m, k = map(int, input().split())
graph = [[[] for _ in range(n)] for _ in range(n)]
for i in range(n):
    data = list(map(int, input().split()))
    for j in range(n):
        if data[j]:
            graph[i][j].append(data[j])

# {player_id:[x, y, d]}
player_xyd = dict()
# {player_id:갖고 있는 총의 공격력}
player_gun = dict()
# {player_id:초기 능력치}
player_skill = dict()
point = [0] * m
for player_id in range(m):
    x, y, d, s = map(int, input().split())
    player_xyd[player_id] = [x-1, y-1, d]
    player_skill[player_id] = s
    # 모든 플레이어는 초기에 총이 없다.
    player_gun[player_id] = 0

# 상/우/하/좌
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

for _ in range(k):
    for player_id in range(m):
        '''1-1'''
        x, y, d = player_xyd[player_id]
        nx, ny = x+dx[d], y+dy[d]
        # 격자를 벗어나는 경우 정반대 방향으로 방향을 바꿔서 1만큼 이동
        if nx<0 or nx>=n or ny<0 or ny>=n:
            d = (d+2)%4
            nx, ny = x + dx[d], y + dy[d]
        player_xyd[player_id] = [nx, ny, d]

        # 이동한 칸의 빈칸 여부
        is_blank = True
        for i in range(m):
            if i != player_id:
                # 이동한 칸에 플레이어가 있는 경우 싸움 시작
                '''2-2-1'''
                if player_xyd[i][:2] == [nx, ny]:
                    fight(player_id, i)
                    is_blank = False
                    break
        '''2-1'''
        if is_blank:
            get_strongest_gun(player_id)

print(' '.join(map(str, point)))
