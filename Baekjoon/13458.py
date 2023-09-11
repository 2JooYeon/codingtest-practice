n = int(input())
student = list(map(int, input().split()))
b, c = map(int, input().split())
answer = 0
for s in student:
    s -= b
    answer += 1
    if s > 0:
        if s%c == 0:
            answer += s//c
        else:
            answer += (s // c + 1)
print(answer)
