n, m = map(int, input().split())
rice = list(map(int, input().split()))

start = 0
end = max(rice)

answer = 0
while (start<=end):
    total = 0
    mid = (start+end)//2
    for x in rice:
        if x > mid:
            total += x-mid
    # 떡을 더 많이 잘라야 하는 경우
    if total < m:
        end = mid-1
    # 떡을 더 적게 잘라야 하는 경우
    else:
        start = mid+1
        answer = mid


print(answer)
