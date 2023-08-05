s = list(map(int, list(input())))
answer = s[0]

for n in s[1:]:
    if answer <= 1 or n <= 1:
        answer += n
    else:
        answer *= n

print(answer)