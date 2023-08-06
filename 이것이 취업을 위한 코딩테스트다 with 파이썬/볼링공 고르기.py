n, m = map(int, input().split())
k = list(map(int, input().split()))
k_set = set(k)
# nC2 조합 경우의 수
answer = n * (n-1) // 2

for w in k_set:
    count = k.count(w)
    if count > 1:
        answer -= count * (count-1) // 2

print(answer)
