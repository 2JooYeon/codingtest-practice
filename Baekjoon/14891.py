from collections import deque


# 회전시킬 톱니바퀴 인덱스 리스트를 반환하는 함수
def check_pole(gear_idx, visited):
    q = deque([])
    q.append(gear_idx)
    visited[gear_idx] = 1
    answer = []
    while q:
        now = q.popleft()
        answer.append(now)
        if now + 1 < 4 and not visited[now + 1] \
            and gear[now][2] != gear[now+1][6]:
            q.append(now+1)
            visited[now+1] = 1
        if now - 1 >= 0 and not visited[now - 1] \
            and gear[now][6] != gear[now-1][2]:
            q.append(now-1)
            visited[now-1] = 1
    return answer


# 톱니바퀴를 회전시키는 함수
def rotate_gear(gear_idx, direction):
    global gear
    # 시계 방향 회전
    if direction == 1:
        temp = [gear[gear_idx][-1]] + gear[gear_idx][:7]
        gear[gear_idx] = temp
    # 반시계 방향 회전
    else:
        temp = gear[gear_idx][1:8] + [gear[gear_idx][0]]
        gear[gear_idx] = temp


gear = []
for _ in range(4):
    gear.append(list(input()))
k = int(input())
for _ in range(k):
    num, direction = map(int, input().split())
    visited = [0] * 4
    # 회전시켜야 하는 톱니바퀴 인덱스 찾기
    target = check_pole(num-1, visited)
    odd = -1
    even = -1
    # 회전시킬 톱니바퀴의 인덱스가 짝수라면 even 활성화
    if (num-1)%2 == 0:
        even = 1
    # 홀수라면 odd 활성화
    else:
        odd = 1
    for n in target:
        # 회전시킬 톱니바퀴의 인덱스가 짝수인지 홀수인지에 따라 even, odd 각각 곱해서 회전 방향 선택
        if n%2 == 0:
            rotate_gear(n, direction*even)
        else:
            rotate_gear(n, direction*odd)

answer = 0
for i in range(4):
    if gear[i][0] == '1':
        answer += 2**i

print(answer)
