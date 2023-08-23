from bisect import bisect_left

n = int(input())
soldier = list(map(int, input().split()))
# 내림차순으로 배치하기 위해 음수로 변환
soldier = [-x for x in soldier]
d = [soldier[0]]
for s in soldier[1:]:
    # 새롭게 들어온 수가 가장 마지막 수보다 작을 때
    if s < d[-1]:
        left = bisect_left(d, s)
        d[left] = s
    # 새롭게 들어온 수가 가장 마지막 수보다 클 때
    elif s > d[-1]:
        d.append(s)

print(n-len(d))
