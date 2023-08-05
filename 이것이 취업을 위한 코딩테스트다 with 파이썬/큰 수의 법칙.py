n, m = map(int, input().split())
answer = min(list(map(int, input().split())))
for _ in range(n-1):
    num = min(list(map(int, input().split())))
    if num > answer:
        answer = num
print(answer)