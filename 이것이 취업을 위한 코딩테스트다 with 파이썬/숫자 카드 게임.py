n, m, k = map(int, input().split())
numbers = list(map(int, input().split()))
numbers.sort(reverse=True)
a = numbers[0]
b = numbers[1]
count = 0
answer = 0
for i in range(m):
    if count != k:
        answer += a
    else:
        answer += b
        count = 0
    count += 1
print(answer)