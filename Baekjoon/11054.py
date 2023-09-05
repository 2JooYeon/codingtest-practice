n = int(input())
arr = list(map(int, input().split()))
rarr = arr[::-1]
d = [1] * n
rd = [1] * n

for i in range(n):
    for j in range(i):
        # 앞의 j번쨰 원소가 i번째 원소보다 작다면
        if arr[j] < arr[i]:
            d[i] = max(d[i], d[j] + 1)
        # 뒤집어진 배열 기준으로 앞의 j번째 원소가 i번째 원소보다 작다면
        if rarr[j] < rarr[i]:
            rd[i] = max(rd[i], rd[j] + 1)

rd = rd[::-1]
answer = 0
for i in range(n):
    answer = max(d[i]+rd[i]-1, answer)

print(answer)