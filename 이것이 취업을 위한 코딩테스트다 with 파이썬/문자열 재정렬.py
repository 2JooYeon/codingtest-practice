s = list(input())
s.sort()
answer = ''
num = 0
for c in s:
    if c.isdigit():
        num += int(c)
    else:
        answer += c

if num != 0:
    print(answer + str(num))
else:
    print(answer)