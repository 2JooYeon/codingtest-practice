from bisect import bisect_left

n = int(input())
arr = list(map(int, input().split()))
# 수열의 길이를 저장할 1차원 리스트
d_len = [1] * n
# 수열을 저장할 1차원 리스트
d_num = [arr[0]]

for i in range(1, n):
    # 새로 들어온 원소가 더 크면
    if arr[i] > d_num[-1]:
        d_num.append(arr[i])
        d_len[i] = len(d_num)
    # 새로 들어온 원소가 더 작으면
    else:
        left = bisect_left(d_num, arr[i])
        d_num[left] = arr[i]
        d_len[i] = left + 1

# 가장 긴 증가하는 부분 수열의 길이
max_len = max(d_len)
print(max_len)
max_idx = d_len.index(max_len)
# 가장 긴 증가하는 부분 수열을 담을 1차원 리스트
answer = []
# 수열의 길이가 가장 긴 인덱스부터 역순으로 answer에 담기
for i in range(max_idx, -1, -1):
    if d_len[i] == max_len:
        answer.append(arr[i])
        max_len -= 1
# 증가하는 순서로 원상 복구
answer = answer[::-1]
print(' '.join(map(str, answer)))
