# m명의 도망자 동시에 움직이는 함수
def move_thief():
    global thief_xyd
    new_thief_xyd = dict()
    for thief_id in thief_xyd:
        tx, ty, td = thief_xyd[thief_id]
        # 술래와의 거리가 3 이하인 도망자만 움직일 수 있다.
        if abs(px-tx) + abs(py-ty) > 3:
            new_thief_xyd[thief_id] = (tx, ty, td)
            continue
        # 현재 바라보고 있는 방향으로 1칸 움직인다.
        nx, ny = tx + dx[td], ty + dy[td]
        nd = td
        # 격자를 벗어나는 경우
        if nx<0 or nx>=n or ny<0 or ny>=n:
            # 방향을 반대로 틀고, 1칸 이동
            nd = (nd+2)%4
            nx, ny = tx + dx[nd], ty + dy[nd]
        # 술래가 없다면 위치 업데이트
        if nx != px or ny != py:
            new_thief_xyd[thief_id] = (nx, ny, nd)
        else:
            new_thief_xyd[thief_id] = (tx, ty, td)
    thief_xyd = new_thief_xyd


# 술래가 도망자를 잡는 함수
def catch_thief(x, y, d):
    global answer
    thief_num = 0
    thief = []
    # 술래의 시야 3칸까지 확인
    for i in range(3):
        if i > 0:
            x += dx[d]
            y += dy[d]
        if x<0 or x>=n or y<0 or y>=n:
            continue
        # 나무 없이 도망자만 있을 경우 체포
        if (x, y) in tree_xy:
            continue
        for thief_id in thief_xyd:
            if thief_xyd[thief_id][:2] == (x, y):
                thief_num += 1
                thief.append(thief_id)
    # 잡힌 도망자는 사라지게 된다.
    for thief_id in thief:
        del thief_xyd[thief_id]
    answer += (step+1) * thief_num


def police_move_outside():
    global px, py, step
    clockwise = True
    for i in range(1, n):
        unit = 2
        if i == n - 1:
            unit = 3
        for _ in range(unit):
            # 감시 방향 (시계로 이동하므로 +1)
            catch_d = (pd + 1) % 4
            for j in range(i):
                # 도망자 모두 이동
                move_thief()
                # 술래 한 칸 이동
                px += dx[pd]
                py += dy[pd]
                # 이동 방향 그대로 감시 진행
                if j <= (i - 2):
                    catch_thief(px, py, pd)
                    step += 1
                    if step == k or len(thief_xyd) == 0:
                        return

            # (0,0)에 도착했을 경우 이동 방향, 감시 방향 틀기
            if px == 0 and py == 0:
                catch_d = (catch_d + 1) % 4
                pd = (pd + 1) % 4
                clockwise = False
            # 이동 방향 업데이트
            pd = (pd + 1) % 4
            # 틀어지는 지점이므로 catch_d 방향으로 감시
            catch_thief(px, py, catch_d)
            step += 1
            if not clockwise or step == k or len(thief_xyd) == 0:
                return


def police_move_inside():
    global px, py, step
    clockwise = False
    for i in range(n - 1, -1, -1):
        unit = 2
        if i == n - 1:
            unit = 3
        for _ in range(unit):
            # 감시 방향 (반시계로 이동하므로 -1)
            catch_d = (pd - 1) % 4
            for j in range(i):
                # 도망자 모두 이동
                move_thief()
                # 술래 한 칸 이동
                px += dx[pd]
                py += dy[pd]
                # 이동 방향 그대로 감시 진행
                if j <= (i - 2):
                    catch_thief(px, py, pd)
                    step += 1
                    if step == k or len(thief_xyd) == 0:
                        return
            # 정중앙에 도착했을 경우 이동 방향, 감시 방향 틀기
            if px == n // 2 and py == n // 2:
                catch_d = (catch_d - 1) % 4
                pd = (pd - 1) % 4
                clockwise = True
            # 이동 방향 업데이트
            pd = (pd - 1) % 4
            # 틀어지는 지점이므로 pd방향으로 감시
            catch_thief(px, py, catch_d)
            step += 1
            if clockwise or step == k or len(thief_xyd) == 0:
                return


# 전체 술래 잡기 플레이
def solution():
    global step, px, py, pd
    clockwise = True
    while True:
        if clockwise:
            for i in range(1, n):
                unit = 2
                if i == n - 1:
                    unit = 3
                for _ in range(unit):
                    # 감시 방향 (시계로 이동하므로 +1)
                    catch_d = (pd + 1) % 4
                    for j in range(i):
                        # 도망자 모두 이동
                        move_thief()
                        # 술래 한 칸 이동
                        px += dx[pd]
                        py += dy[pd]
                        # 이동 방향 그대로 감시 진행
                        if j <= (i - 2):
                            catch_thief(px, py, pd)
                            step += 1
                            if step == k or len(thief_xyd) == 0:
                                return

                    # (0,0)에 도착했을 경우 이동 방향, 감시 방향 틀기
                    if px == 0 and py == 0:
                        catch_d = (catch_d + 1) % 4
                        pd = (pd + 1) % 4
                        clockwise = False
                    # 이동 방향 업데이트
                    pd = (pd + 1) % 4
                    # 틀어지는 지점이므로 catch_d 방향으로 감시
                    catch_thief(px, py, catch_d)
                    step += 1
                    if step == k or len(thief_xyd) == 0:
                        return
                    if clockwise == False:
                        break
                if clockwise == False:
                    break

        else:
            for i in range(n - 1, -1, -1):
                unit = 2
                if i == n - 1:
                    unit = 3
                for _ in range(unit):
                    # 감시 방향 (반시계로 이동하므로 -1)
                    catch_d = (pd - 1) % 4
                    for j in range(i):
                        # 도망자 모두 이동
                        move_thief()
                        # 술래 한 칸 이동
                        px += dx[pd]
                        py += dy[pd]
                        # 이동 방향 그대로 감시 진행
                        if j <= (i - 2):
                            catch_thief(px, py, pd)
                            step += 1
                            if step == k or len(thief_xyd) == 0:
                                return
                    # 정중앙에 도착했을 경우 이동 방향, 감시 방향 틀기
                    if px == n // 2 and py == n // 2:
                        catch_d = (catch_d - 1) % 4
                        pd = (pd - 1) % 4
                        clockwise = True
                    # 이동 방향 업데이트
                    pd = (pd - 1) % 4
                    # 틀어지는 지점이므로 pd방향으로 감시
                    catch_thief(px, py, catch_d)
                    step += 1
                    if step == k or len(thief_xyd) == 0:
                        return
                    if clockwise:
                        break
                if clockwise:
                    break


# 격자 크기, 도망자 수, 나무 수, 라운드 수
n, m, h, k = map(int, input().split())
# 도망자 위치와 이동 방향 저장
thief_xyd = dict()
for i in range(m):
    x, y, d = map(int, input().split())
    thief_xyd[i] = (x-1, y-1, d)
# 나무 위치 저장
tree_xy = dict()
for _ in range(h):
    x, y = map(int, input().split())
    tree_xy[(x-1, y-1)] = 1
# 술래의 위치와 이동 방향 저장
px, py, pd = n//2, n//2, 0

# 상/우/하/좌
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

step = 0
answer = 0
solution()
print(answer)
