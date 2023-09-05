n, s = map(int, input().split())
arr = list(map(int, input().split()))

answer = int(1e9)
interval_sum = 0
end = 0

# start를 증가시키며 이동
for start in range(n):
    # 부분합이 s 미만이고, end를 가능한 만큼 이동
    while interval_sum < s and end < n:
        interval_sum += arr[end]
        end += 1
    if interval_sum >= s:
        answer = min(answer, end-start)
    interval_sum -= arr[start]

if answer == int(1e9):
    print(0)
else:
    print(answer)