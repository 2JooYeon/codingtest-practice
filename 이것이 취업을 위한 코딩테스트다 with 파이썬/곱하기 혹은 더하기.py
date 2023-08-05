s = list(map(int, list(input())))
answer = 0
eval_flag = 0

if len(s) == 1:
    answer = s[0]

else:
    for n in s:
        if n == 0 or answer == 0:
            answer += n
        else:
            answer *= n

print(answer)