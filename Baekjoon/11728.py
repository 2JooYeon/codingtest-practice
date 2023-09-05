n, m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

result = [0] * (n+m)
i, j, k = 0, 0, 0

while i<n or j<m:
    # b의 모든 원소를 처리했거나, a의 원소가 더 작을 때
    if j>=m or (i<n and a[i] <= b[j]):
        result[k] = a[i]
        i += 1
    # a의 모든 원소를 처리했거나, b의 원소가 더 작을 때
    else:
        result[k] = b[j]
        j += 1
    k += 1

for num in result:
    print(num, end=' ')
