n = int(input())
fear = list(map(int, input().split()))
answer = 0

fear.sort(reverse=True)
i = fear[0]
count = 0

while True:
    if count + i < n:
        answer += 1
        count += i
        i = fear[count]
    elif count + i == n:
        answer += 1
        break
    else:
        break
print(answer)