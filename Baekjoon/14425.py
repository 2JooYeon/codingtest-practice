n, m = map(int, input().split())
# 빠른 탐색을 위해 딕셔너리 사용
s = dict()
answer = 0
for _ in range(n):
    s[input()] = 1

for _ in range(m):
    data = input()
    if data in s:
        answer += 1

print(answer)