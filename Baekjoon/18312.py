n, k = input().split()
answer = 0
for hour in range(int(n)+1):
    for minute in range(60):
        for second in range(60):
            if k in str(hour).rjust(2, '0') + str(minute).rjust(2, '0')+ str(second).rjust(2, '0'):
                answer += 1

print(answer)
