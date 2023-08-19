n = int(input())
answer = []
for _ in range(n):
    answer.append(int(input()))
answer.sort(reverse=True)
for num in answer:
    print(num, end=' ')