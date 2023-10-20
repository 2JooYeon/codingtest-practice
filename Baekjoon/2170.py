import sys
input = sys.stdin.readline

n = int(input())
line = []
for _ in range(n):
    x, y = map(int, input().split())
    line.append((x, y))

line.sort(key=lambda x:x[0])
end = line[0][1]
answer = end - line[0][0]


for i in range(1, n):
    x, y = line[i]
    # 새로 그으려는 선이 이전 선과 떨어져 있을때
    if x > end:
        # 새롭게 그리는 선의 길이를 추가
        answer += (y-x)
    # 새로 그으려는 선이 이전 선과 겹칠 때
    else:
        # 새로 그은 선의 전체가 겹치는 경우에는 아무 일도 일어나지 않는다.
        if end >= y:
            continue
        # 추가로 그은 선의 길이만 추가
        answer += (y-end)
    end = max(y, end)

print(answer)